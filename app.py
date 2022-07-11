from flask import Flask, render_template, request, jsonify

from env import PORT, MONGO_URL, DATABASE_NAME, COLLECTION_USER
from database import getMongoClient

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
    name = request.form['name']
    password = request.form['password']
    
    database[COLLECTION_USER].find_one({}) # 중복 검사
    database[COLLECTION_USER].insert_one({}) # 아이디 생성

    return jsonify({
        'msg': 'hello'
    })

@app.route('/api/login', methods=['POST'])
def apiLogin():
    name = request.form['name']
    password = request.form['password']

    return jsonify({
        'msg': 'hello'
        # 'msg': [ name, password ]
    })

if __name__ == '__main__':
    app.run(
        '0.0.0.0',
        port=PORT,
        debug=True)