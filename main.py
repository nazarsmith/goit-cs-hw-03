from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://user:passwordx@cluster.aabb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster",
    server_api=ServerApi("1"),
)

db = client.book


def loose_id(result: dict):
    """a helper function"""
    result.pop("_id")
    return result


def notify_user(result):
    """a helper function"""
    if "modified_count" in dir(result) and result.modified_count:
        print("Done.")
        return
    elif "deleted_count" in dir(result) and result.deleted_count:
        print("Done.")
        return
    print("Update/Deletion failed.")


def find_all():
    result = db.cats.find()
    print("\n".join([str(loose_id(el)) for el in result]))


def find_one_by_name():
    print("\nAttempting to look up a cat by name..")
    result = db.cats.find_one({"name": input("Enter the name of a cat: ")})
    if not result:
        print("Not found.")
        return
    print(loose_id(result))


def insert_one(name: str, age: int, features: list[str]):

    result_one = db.cats.insert_one(
        {
            "name": name,
            "age": age,
            "features": features,
        }
    )

    print(result_one.inserted_id)


def update_age_by_name(name: str, age: int):
    print("\nAttenmpting to update an entry..")
    result = db.cats.update_one({"name": name}, {"$set": {"age": age}})
    notify_user(result)


def update_features_by_name(name: str, feature: str):
    print("\nAttenmpting to update an entry..")
    result = db.cats.update_one({"name": name}, {"$push": {"features": feature}})
    notify_user(result)


def delete_by_name(name: str):
    print("\nAttenmpting to delete an entry..")
    result = db.cats.delete_one({"name": name})
    notify_user(result)


def delete_all():
    print("\nAttenmpting to delete all the entries..")
    result = db.cats.delete_many({})
    notify_user(result)


if __name__ == "__main__":
    insert_one(name="Murka", age=18, features=["fluffy", "has no teeth", "meows a lot"])
    insert_one(name="Barsik", age=3, features=["fluffy", "likes meat", "affectionate"])
    find_all()
    find_one_by_name()
    update_age_by_name(name="Murka", age=11)
    find_all()
    update_features_by_name("Murka", "likes to eat meat")
    find_all()
    delete_by_name("Murka")
    find_all()
    delete_all()
    find_all()
