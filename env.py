from json import load
from dotenv import load_dotenv
import os

load_dotenv()

port = os.environ.get('port')