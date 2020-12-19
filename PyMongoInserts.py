import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017")

db = cluster["school"]
collection = db["students"]

collection.insert_many([

{

    "userId" : 6,
    "firstName" : "Abhi",
    "lastName" : "Sri",
    "phoneNumber" : "8600",
    "emailAddress" : "abhi@1.com",
    "Gender" : "Male",
    "Age" : 30.0
},
{

    "userId" : 7,
    "firstName" : "Prachi",
    "lastName" : "Kud",
    "phoneNumber" : "9876",
    "emailAddress" : "pra@a.com",
    "Gender" : "Female",
    "Age" : 28
}
])
