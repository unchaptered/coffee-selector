from flask import Flask, render_template, request, jsonify, redirect

from modules.env import PORT, MONGO_URL, DATABASE_NAME, COLLECTION_USER, COLLECTION_CAPSULE, TOKEN_SECRET, TOKEN_ALGORITHM
from modules.database import getMongoClient
from modules.form import getSuccessForm, getFailureForm

from modules.tokenizer import getToken
from modules.validate import validate_name, validate_password

app = Flask(__name__)
database = getMongoClient(MONGO_URL)[DATABASE_NAME]

# 아이디 비밀번호 서버이름으로 변경해야함
app = Flask(__name__)

@app.route('/result',methods=["GET"])
def result_list():
    # arrays_property=request.form['uesrs_choose']
    # list=list(DATABASE_NAME.articles.find({'writer':[arrays_property.winter]}))
    list=[{'name':'n1','desc':'d1','option':'o1'},{'name':'n2','desc':'d2','option':'o2'}]
    return render_template('/pages/result.html', list=list, title='캡슐커피 취향저격')


@app.route('/join', methods=['GET'])
def join():
    return render_template('./pages/join.html', title='캡슐커피 취향저격')

@app.route('/login', methods=['GET'])
def login():

    name = request.args.get('name')

    if name is not None:
        return render_template('./pages/login.html', name=name, title='캡슐커피 취향 저격')
    else:
        return render_template('./pages/login.html', title='캡슐커피 취향저격')

@app.route('/api/join', methods=['POST'])
def apiJoin():

    name = validate_name(request.form['name'])
    password = validate_password(request.form['password'])

    if name is None or password is None:
        return jsonify(
            getFailureForm('유효하지 않는 가입을 전달 받았습니다.', {
                'name': name,
                'password': password
            })
        )

    # 중복 검사
    find = database[COLLECTION_USER].find_one({
        'name': name,
        'password': password
    })

    if find is not None:
        # 이미 중복된 사용자가 존재하는 경우, -> 회원가입 실패
        return jsonify(
            getFailureForm('이미 중복된 사용자가 존재합니다.')
        );
    else:
        # 이미 중복된 사용자가 없는 경우 -> 회원가입 실행
        insert = database[COLLECTION_USER].insert_one({
            'name': name,
            'password': password
        })

        # 이미 중복된 사용자가 없는 경우 -> 회원가입 성공
        return jsonify(
            getSuccessForm('회원가입에 성공하셨습니다.', { 
                'name': name,
                'password': password
            })
        );

@app.route('/api/login', methods=['POST'])
def apiLogin():

    name = validate_name(request.form['name'])
    password = validate_password(request.form['password'])

    if name is None or password is None:
        return jsonify(
            getFailureForm('유효하지 않는 가입을 전달 받았습니다.')
        )

    find = database[COLLECTION_USER].find_one({
        'name': name,
        'password': password
    })

    if find is not None:
        token = getToken({ 'name': name }, TOKEN_SECRET, TOKEN_ALGORITHM )
        return jsonify(
            getSuccessForm('로그인에 성공하셨습니다.', {
                'name': name,
                'password': password,
                'accessToken': token
            })
        )
    else:
        return jsonify(
            getFailureForm('로그인에 실패하셨습니다.')
        )

    

if __name__ == '__main__':

    app.run(
        '0.0.0.0',
        port=PORT,
        debug=True)