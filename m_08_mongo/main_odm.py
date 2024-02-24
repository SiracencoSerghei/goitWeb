from mongoengine import *
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.joinpath(".env")
if env_path.is_file:
    print(env_path)
    load_dotenv(env_path)

MONGODB_USER = os.getenv("MONGODB_USER")
MONGODB_PASS = os.getenv("MONGODB_PASS")
MONGODB_HOST = os.getenv("MONGODB_HOST")
MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB_NAME = os.getenv("MONGODB_NAME")

client = None
URI = None

if MONGODB_USER:
    URI = f"{MONGODB_URL}?retryWrites=true&w=majority&appName=Cluster0"

connect(
    db="cats",
    host=URI,
)


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
    meta = {"allow_inheritance": True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()


if __name__ == "__main__":
    ross = User(email="ross@example.com", first_name="Ross", last_name="Lawley").save()

    john = User(email="john@example.com")
    john.first_name = "John"
    john.last_name = "Lawley"
    john.save()

    post1 = TextPost(title="Fun with MongoEngine", author=john)
    post1.content = "Took a look at MongoEngine today, looks pretty cool."
    post1.tags = ["mongodb", "mongoengine"]
    post1.save()

    post2 = LinkPost(title="MongoEngine Documentation", author=ross)
    post2.link_url = "http://docs.mongoengine.com/"
    post2.tags = ["mongoengine"]
    post2.save()
