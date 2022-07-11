from json import load
from dotenv import load_dotenv
import os

load_dotenv()

PORT = os.environ.get('PORT')
MONGO_URL = os.environ.get('MONGO_URL')
DATABASE_NAME = os.environ.get('DATABASE_NAME')

COLLECTION_USER = os.environ.get('COLLECTION_USER')