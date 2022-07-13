from flask_bcrypt import Bcrypt

def getBcrypt(app: any) -> Bcrypt:
    """
    FLask 전용 암호화 모듈인 Brypt-Flask 를 이용하였습니다.

    함수 실행시 암호화 모듈이 리턴됩니다.

    공식문서 : https://github.com/mahenzon/flask-bcrypt
    """
    return Bcrypt(app)