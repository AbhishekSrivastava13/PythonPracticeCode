import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017")

db = cluster["school"]
collection = db["students"]

results = collection.find({"firstName":"Abhi","userId":6}) # here , plays AND operator

for result in results:
    print(result)