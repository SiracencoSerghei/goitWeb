from pathlib import Path
import os
from datetime import date
import enum
from dotenv import load_dotenv
from fastapi import HTTPException, status

from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    Date,
    DateTime,
    Integer,
    String,
    Text,
    ForeignKey,
    func,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError

domain = os.getenv("POSTGRES_HOST")
if not domain:
    ENV_FILE = Path(__file__).resolve().parent.parent.parent.joinpath(".env")
    load_dotenv(ENV_FILE)
    domain = os.getenv("POSTGRES_HOST")
    print(f"{ENV_FILE=} {domain=}")

username = os.getenv("POSTGRES_USERNAME")
password = os.getenv("POSTGRES_PASSWORD")
domain = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
database = os.getenv("POSTGRES_DATABASE")

URI = None
if domain:
    URI = f"postgresql+psycopg2://{username}:{password}@{domain}:{port}/{database}"

SQLALCHEMY_DATABASE_URL = URI

print(f"{SQLALCHEMY_DATABASE_URL=}")
print(f"{port=}")

assert SQLALCHEMY_DATABASE_URL is not None, "SQLALCHEMY_DATABASE_URL UNDEFINED"

Base = declarative_base()


class Role(enum.Enum):
    admin: str = "admin"  # type: ignore
    moderator: str = "moderator"  # type: ignore
    user: str = "user"  # type: ignore


class User(Base):
    __tablename__ = "users"

    id: int | Column[int] = Column(Integer, primary_key=True)
    username: str | Column[str] = Column(String(150), nullable=False)
    email: str | Column[str] = Column(String(150), nullable=False, unique=True)
    password: str | Column[str] = Column(String(255), nullable=False)
    refresh_token: str | Column[str] | None = Column(String(255), nullable=True)
    avatar: str | Column[str] | None = Column(String(255), nullable=True)
    role: Enum | Column[Enum] = Column("roles", Enum(Role), default=Role.user)

    def __str__(self):
        return f"id: {self.id}, email: {self.email}, username: {self.username}"

class Contact(Base):

    __tablename__ = "contacts"

    id: int | Column[int] = Column(Integer, primary_key=True, index=True)
    first_name: str | Column[str] | None = Column(String)
    last_name: str | Column[str] | None = Column(String)
    email: str | Column[str] = Column(String)
    phone: str | Column[str] | None = Column(String)
    birthday: date | Column[date] | None = Column(Date)
    comments: str | Column[str] | None = Column(Text)
    favorite: bool | Column[bool] | None = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    user_id: int | Column[int] = Column(
        Integer, ForeignKey("users.id"), nullable=False, default=1
    )
    user = relationship("User", backref="contacts")
    # , cascade="all, delete-orphan"


engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db():
    db = DBSession()
    try:
        yield db
    except SQLAlchemyError as err:
        print(err)
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    finally:
        db.close()


if __name__ == "__main__":
    print(engine)
