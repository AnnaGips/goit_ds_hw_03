from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до локального екземпляра MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Вибір або створення бази даних
db = client["cats_db"]

# Вибір або створення колекції
collection = db["cats"]

def create_cat(name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        result = collection.insert_one(cat)
        print(f"Created cat with id: {result.inserted_id}")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"An error occurred: {e}")

def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("No cat found with that name.")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_cat_age(name, new_age):
    try:
        result = collection.update_one(
            {"name": name},
            {"$set": {"age": new_age}}
        )
        if result.modified_count > 0:
            print(f"Updated age for cat named {name}.")
        else:
            print(f"No cat found with the name {name}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_feature_to_cat(name, new_feature):
    try:
        result = collection.update_one(
            {"name": name},
            {"$addToSet": {"features": new_feature}}
        )
        if result.modified_count > 0:
            print(f"Added new feature to cat named {name}.")
        else:
            print(f"No cat found with the name {name}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Deleted cat named {name}.")
        else:
            print(f"No cat found with the name {name}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Deleted {result.deleted_count} cats.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Приклади використання функцій

    # Створення нових котів
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat("murzik", 5, ["ловить мишей", "любить спати"])

    # Читання всіх котів
    print("\nВсі коти в базі даних:")
    read_all_cats()

    # Читання кота за ім'ям
    print("\nІнформація про кота на ім'я 'barsik':")
    read_cat_by_name("barsik")

    # Оновлення віку кота
    update_cat_age("barsik", 4)

    # Додавання нової характеристики
    add_feature_to_cat("barsik", "любить їсти")

    # Видалення кота за ім'ям
    delete_cat_by_name("murzik")

    # Видалення всіх котів
    delete_all_cats()
