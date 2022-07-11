import os

from dotenv import load_dotenv

load_dotenv()

port = os.environ.get('port')
 # No newline at end of file
PORT = os.environ.get('PORT')
MONGO_URL = os.environ.get('MONGO_URL')
DATABASE_NAME = os.environ.get('DATABASE_NAME')

COLLECTION_USER = os.environ.get('COLLECTION_USER')
 # No newline at end of file