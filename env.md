# env

특정한 값은 환경 변수로 선언하여 저장해두어야 합니다.
아래와 같은 형태로 값을 저장해두었고 이를 env.py 에서 로드하고 있습니다.

```env
key = value
```

## port

로컬 환경에서 사용할 port 번호를 port = 0000 의 형태로 .env 파일 안에 넣어주세요.

```env
port = 0000

# For database
MONGO_URL = 'MongoDB 접속용 URL'
DATABASE_NAME = 'MongoDB 데이터베이스 이름'
COLLECTION_USER = 'users'
COLLECTION_CAPSULE = 'capsules'

# For Tokenizer
TOKEN_SECRET = '암호화 키'
TOKEN_ALGORITHM = '알고리즘 방식'
[//]: # 필요 시 추가 하고 해당 env.md 와 env.py 에 변수 추가해주세요 :) ()
```