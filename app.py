from flask import Flask, render_template, request, jsonify

from modules.env import PORT, MONGO_URL, DATABASE_NAME, COLLECTION_USER, COLLECTION_CAPSULE, TOKEN_SECRET, TOKEN_ALGORITHM
from modules.database import getMongoClient
from modules.form import getSuccessForm, getFailureForm

from modules.tokenizer import getToken
from modules.validate import validate_name, validate_password

app = Flask(__name__)
database = getMongoClient(MONGO_URL)[DATABASE_NAME]

#결과창
@app.route('/result',methods=["GET"])
def result_list():
    # querys=requests.form('questions')
    # arrays_pro    perty=request.form['uesrs_choose']
    # list=list(DATABASE_NAME.articles.find({'writer':[arrays_property.winter]}))
    # querys=[{'name':'n1','desc':'d1','option':'o1'}]
    coffees=list(database[COLLECTION_CAPSULE].find({},{'_id':False}))
    print(len(coffees))
    return render_template('/pages/result.html', list=coffees, title='캡슐커피 취향저격')

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

@app.route('/nespresso', methods=['GET'])
def show_nespresso():
    name = request.form['name']
    return render_template('./pages/select.html', title='캡슐커피 취향저격',name=name)

@app.route("/nespresso", methods=["POST"])
def save_nespresso():
    cake_receive = request.form['cake_give']
    apple_receive = request.form['apple_give']
    strength_receive = request.form['strength_give']
    milk_receive = request.form['milk_give']
    size_receive = request.form['size_give']

    doc = {
        'cake': cake_receive,
        'apple': apple_receive,
        'strength': strength_receive,
        'milk': milk_receive,
        'size': size_receive
    }
    database.COLLECTION_CAPSULE.insert_one(doc)

    return jsonify({'msg': '선택 완료!'})

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == '__main__':

    app.run(
        '0.0.0.0',
        port=PORT,
        debug=True)