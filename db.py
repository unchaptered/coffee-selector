from src.modules.provider.mongo_provider import getDatabase, getUserConnection, getSelectConnection, getCapsuleConnection
from src.modules.config.config_provider import MONGO_URL, DATABASE_NAME

database = getDatabase(MONGO_URL, DATABASE_NAME);

def getUserConnection():
    return getUserConnection(database)

def getCapsuleConnection():
    return getCapsuleConnection(database)

def getSelectConnection():
    return getSelectConnection(database)
