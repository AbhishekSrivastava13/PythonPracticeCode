import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017")

db = cluster["school"]
collection = db["students"]

results = collection.update_many({"userId":6}, {"$set":{"lastName":"Srivastava"}})