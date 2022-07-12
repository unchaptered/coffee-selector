from dotenv import load_dotenv
import os

load_dotenv()                                               # .env 형식의 파일에서 변수값을 추출합니다.

PORT = os.environ.get('PORT')                               # 서버 실행 포트
MONGO_URL = os.environ.get('MONGO_URL')                     # MongoDB Atlas URL 경로
DATABASE_NAME = os.environ.get('DATABASE_NAME')             # MongoDB Atlas DB 이름

COLLECTION_USER = os.environ.get('COLLECTION_USER')         # MongoDB Atlas Collection 이름
COLLECTION_CAPSULE = os.environ.get('COLLECTION_CAPSULE')   # MongoDB Atlas Collection 이름

TOKEN_SECRET = os.environ.get('TOKEN_SECRET')
TOKEN_ALGORITHM = os.environ.get('TOKEN_ALGORITHM')