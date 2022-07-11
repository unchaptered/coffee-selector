from flask import Flask, render_template, request, jsonify
<<<<<<< HEAD
from env import port
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
=======

import json
from modules.env import PORT, MONGO_URL, DATABASE_NAME, COLLECTION_USER, COLLECTION_CAPSULE
from modules.database import getMongoClient
from modules.form import getSuccessForm, getFailureForm

>>>>>>> d04a1b2b3c06f27d951d827d13b0c27a48d1b5ad
app = Flask(__name__)
database = getMongoClient(MONGO_URL)[DATABASE_NAME]

# 아이디 비밀번호 서버이름으로 변경해야함
db = client.dbsparta
app = Flask(__name__)


@app.route('/result',methods=["GET"])
def result_list():
    arrays_property=request.form['uesrs_choose']
    list=list(db.articles.find({'writer':[arrays_property.winter]}))

    return render_template('/pages/result.html', list=list, title='캡슐커피 취향저격')
#결과보내기 test
# @app.route('/api/scrap-nespresso')
# def scrap_nespresso():
#     name=request.args.get("name")
#     return render_template('/pages/scrap-nespresso.html',name=name)
#


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

    return jsonify(
        getSuccessForm('회원가입에 성공하셨습니다.', {
            'name': name,
            'password': password
        })
    );

@app.route('/api/login', methods=['POST'])
def apiLogin():
    name = request.form['name']
    password = request.form['password']

    return jsonify(
        getSuccessForm('로그인에 성공하셨습니다.'), {
            'name': name,
            'password': password
        }
    )

if __name__ == '__main__':

    app.run(
        '0.0.0.0',
        port=PORT,
        debug=True)