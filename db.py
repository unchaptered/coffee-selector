from src.modules.provider.mongo_provider import getDatabase, getUserConnection, getSelectConnection, getCapsuleConnection
from src.modules.config.config_provider import MONGO_URL, DATABASE_NAME

database = getDatabase(MONGO_URL, DATABASE_NAME);

def getUser():
    return getUserConnection(database)

def getCapsule():
    return getCapsuleConnection(database)

def getSelect():
    return getSelectConnection(database)