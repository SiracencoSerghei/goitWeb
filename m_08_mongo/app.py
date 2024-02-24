import argparse
import os
from pathlib import Path
from bson import ObjectId
from dotenv import load_dotenv
import pymongo

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

    try:
        client = pymongo.MongoClient(URI)
    except pymongo.errors.ConfigurationError:
        print(
            "An Invalid URI host error was received. Is your Atlas host name correct in your connection string?"
        )
    except pymongo.errors as e:
        print("pymongo error:", e)
else:
    print("not defined MONGODB_USER. Database not connected")

print(f"{client=}")
print(f"{URI=}")
# testing connect
db = client[f"{MONGODB_NAME}"]
collection = db["cats"]

parser = argparse.ArgumentParser(description="Server Cats Enterprise")
parser.add_argument("--action", help="create, update, read, delete")  # CRUD action
parser.add_argument("--id")
parser.add_argument("--name")
parser.add_argument("--age")
parser.add_argument("--features", nargs="+")

arg = vars(parser.parse_args())

action = arg.get("action")
pk = arg.get("id")
name = arg.get("name")
age = arg.get("age")
features = arg.get("features")


def find():
    return db.cats.find()


def create(name, age, features):
    r = db.cats.insert_one(
        {
            "name": name,
            "age": age,
            "features": features,
        }
    )
    return r


def update(pk, name, age, features):
    r = db.cats.update_one(
        {"_id": ObjectId(pk)},
        {
            "$set": {
                "name": name,
                "age": age,
                "features": features,
            }
        },
    )
    return r


def delete(pk):
    return db.cats.delete_one({"_id": ObjectId(pk)})


def main():
    match action:
        case "create":
            r = create(name, age, features)
            print(r)
        case "read":
            r = find()
            print([e for e in r])
        case "update":
            r = update(pk, name, age, features)
            print(r)
        case "delete":
            r = delete(pk)
            print(r)
        case _:
            print("Unknown command")


if __name__ == "__main__":

    main()
