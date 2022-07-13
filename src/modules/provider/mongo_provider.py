from pymongo import MongoClient, Database
from ..config.config_provider import COLLECTION_USER, COLLECTION_CAPSULE, COLLECTION_SELECT

def getMongoClient(MONGO_URL):
    """
    지정된 MONGO_URL 을 사용하여 MongoDB Atlas 서버와 연결을 하게 됩니다.
    @depreacted
    """
    return MongoClient(MONGO_URL)

def getDatabase(MONGO_URL: str, DATABASE_NAME: str) -> Database:
    return MongoClient(MONGO_URL)[DATABASE_NAME]

def getUserConnection(database: Database):
    return database[COLLECTION_USER]

def getCapsuleConnection(database: Database):
    return database[COLLECTION_CAPSULE]

def getSelectConnection(database: Database):
    return database[COLLECTION_SELECT]
