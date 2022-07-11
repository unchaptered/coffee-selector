from flask import Flask, render_template, request, jsonify

import json
from modules.env import PORT, MONGO_URL, DATABASE_NAME, COLLECTION_USER, COLLECTION_CAPSULE
from modules.database import getMongoClient

app = Flask(__name__)
database = getMongoClient(MONGO_URL)[DATABASE_NAME]

@app.route('/')
def home():
    return render_template('index.html', title='캡슐커피 취향저격')

@app.route('/join', methods=['GET'])
def join():
    return render_template('./pages/join.html', title='캡슐커피 취향저격')

@app.route('/login', methods=['GET'])
def login():
    return render_template('./pages/login.html', title='캡슐커피 취향저격')


@app.route('/api/join', methods=['POST'])
def apiJoin():
    body = json.loads(request.get_data(), encoding='utf-8')

    name = body['name']
    password = body['password']

    # 중복 검사
    find = database[COLLECTION_USER].find_one({
        'name': name,
        'password': password
    })
    print(find) # value of None

    # 회원 가입
    insert = database[COLLECTION_USER].insert_one({
        'name': name,
        'password': password
    })
    print(insert)

    return jsonify({
        'isSuccess': True,
        'message': '회원가입에 성공하셨습니다.',
        'result': {}
    })

@app.route('/api/login', methods=['POST'])
def apiLogin():
    name = request.form['name']
    password = request.form['password']

    return jsonify({
        'isSuccess': True,
        'message': '로그인에 성공하셨습니다.',
        'result': {}
    })

if __name__ == '__main__':
    app.run(
        '0.0.0.0',
        port=PORT,
        debug=True)