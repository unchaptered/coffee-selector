from pymongo import MongoClient

def getMongoClient(MONGO_URL):
    return MongoClient(MONGO_URL)