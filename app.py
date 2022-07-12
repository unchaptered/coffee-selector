from flask import Flask, render_template, request, jsonify, redirect

import json
from modules.env import PORT, MONGO_URL, DATABASE_NAME, COLLECTION_USER, COLLECTION_CAPSULE
from modules.database import getMongoClient
from modules.form import getSuccessForm, getFailureForm

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
    return render_template('./pages/login.html', title='캡슐커피 취향저격')

@app.route('/api/join', methods=['POST'])
def apiJoin():

    name = request.form['name']
    password = request.form['password']

    # 중복 검사
    find = database[COLLECTION_USER].find_one({
        'name': name,
        'password': password
    })
    print(find)

    if find is not None:
        # 이미 중복된 사용자가 존재하는 경우, -> 회원가입 실패
        return jsonify(
            getSuccessForm('이미 중복된 사용자가 존재합니다.', {
                'name': name,
                'password': password
        }));
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

    name = request.form['name']
    password = request.form['password']

    find = database[COLLECTION_USER].find_one({
        'name': name,
        'password': password
    })

    if find is not None:
        return jsonify(
            getSuccessForm('로그인에 성공하셨습니다.', {
                'name': name,
                'password': password
            })
        )
    else:
        return jsonify(
            getFailureForm('로그인에 실패하셨습니다.', {
                'name': name,
                'password': password
            })
        )

    

if __name__ == '__main__':

    app.run(
        '0.0.0.0',
        port=PORT,
        debug=True)