from flask_bcrypt import Bcrypt

def getBcrypt(app: any) -> Bcrypt:
    """
    FLask 전용 암호화 모듈인 Brypt-Flask 를 이용하였습니다.

    함수 실행시 암호화 모듈이 리턴됩니다.

    공식문서 : https://github.com/mahenzon/flask-bcrypt
    """
    return Bcrypt(app)


def getHashPw(brcypt: Bcrypt, pw: str):
    """
    getBcrypt 함수를 통해서 생성된 Brypt 모듈을 사용하여 암호화 pw 를 생성합니다.

    기존의 내장 함수는 Binary 타입의 변수를 떨구기 때문에,

    decode('ascii) 부분으로 문자열 타입으로 변환하였습니다.
    """
    return brcypt.generate_password_hash('pw').decode('ascii')