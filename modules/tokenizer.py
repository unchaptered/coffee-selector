import jwt

def getToken(data: dict, key: str, algorithm: str):
    return jwt.encode(data, key, algorithm)