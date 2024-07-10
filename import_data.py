import json
from pymongo import MongoClient

# Завантаження даних з файлів
with open('quotes.json') as f:
    quotes_data = json.load(f)

with open('authors.json') as f:
    authors_data = json.load(f)

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["quotes_db"]

# Імпорт даних у колекції
db.quotes.insert_many(quotes_data)
db.authors.insert_many(authors_data)
