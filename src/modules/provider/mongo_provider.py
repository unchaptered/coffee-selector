from pymongo import MongoClient

def getMongoClient(MONGO_URL):
    """
    지정된 MONGO_URL 을 사용하여 MongoDB Atlas 서버와 연결을 하게 됩니다.
    """
    return MongoClient(MONGO_URL)