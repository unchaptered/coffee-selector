from flask import Flask, redirect, render_template, request, jsonify, url_for

# Provider : 특정 기능을 공급하는 함수들
from db import getUser, getSelect, getCapsule
from src.modules.provider.form_provider import getSuccessForm, getFailureForm 
from src.modules.config.config_provider import PORT, TOKEN_SECRET, TOKEN_ALGORITHM

# Validator : 특정 값의 유효성을 테스트하는 함수들
from src.modules.vadliator.form_validator import validate_name, validate_password
# Tokenizer : 토큰을 생성하는 함수
from src.modules.auth.tokenizer import getToken
from src.modules.auth.bcrypt import getBcrypt

app = Flask(__name__)

# 결과창
@app.route('/result', methods=["GET"])
def result_list():
    doc={
        'cake_receive' : request.form['cake_give'],
        'apple_receive' : request.form['apple_give'],
        'strength_receive' : request.form['strength_give'],
        'milk_receive' : request.form['milk_give'],
        'size_receive' : request.form['size_give'],
    }
    def taste(doc):
        strong_sum=0
        for i in doc:
            strong_sum+=2-int(i)
        if strong_sum > 5:
            strong_sum=5;
        if strong_sum<0:
            strong_sum=0;
        bitter_sum=0
        for i in doc:
            strong_sum+=2-int(i)
        if strong_sum > 5:
            strong_sum=5;
        if strong_sum<0:
            strong_sum=0;strong_sum=0
        for i in doc:
            strong_sum+=2-int(i)
        if strong_sum > 5:
            strong_sum=5;
        if strong_sum<0:
            strong_sum=0;

    coffees=list(getCapsule().find({},{'_id':False}))
    print(len(coffees))
    return render_template('/pages/result.html',list=querys, title='캡슐커피 취향저격', user_name='name')

@app.route('/api/result',methods=["POST"])
def saver_cof():
    print('checkapi')
    cof_name=request.form['cof_name']
    user_name=request.form['user_name']
    print(cof_name,user_name)
    find = getSelect().find_one({
        'user_name': user_name,
    })

    if find is not None:
        # 전에 선택했던 사용자인 경우
        getSelect().update_one({'user_name':user_name},{'$set':{'cof_name':cof_name}})
    else:
        # 사용한 기록이 없는 사용자안 경우 -> 기록
        insert = getSelect().insert_one({
            'user_name': user_name,
            'cof_name': cof_name
        })
    return jsonify(
            getSuccessForm('기록성공', {
                'name':user_name,
                'cof_name': cof_name,
            })
        )

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

@app.route('/login/guest', methods=['GET'])
def login_as_guest():
    return redirect(url_for('select'));

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

    hashed_password = getBcrypt(app).generate_password_hash(password).decode('ascii')

    print(name, password, hashed_password)
    # 중복 검사
    find = getUser().find_one({
        'name': name,
        'password': hashed_password
    })

    if find is not None:
        # 이미 중복된 사용자가 존재하는 경우, -> 회원가입 실패
        return jsonify(
            getFailureForm('이미 중복된 사용자가 존재합니다.')
        );
    else:
        # 이미 중복된 사용자가 없는 경우 -> 회원가입 실행
        insert = getUser().insert_one({
            'name': name,
            'password': hashed_password
        })

        # 이미 중복된 사용자가 없는 경우 -> 회원가입 성공
        return jsonify(
            getSuccessForm('회원가입에 성공하셨습니다.', { 
                'name': name,
                'password': '비공개'
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

    hashed_password = getBcrypt(app).generate_password_hash(password).decode('ascii')

    find = getUser().find_one({
        'name': name,
        'password': hashed_password
    })

    if find is not None:
        token = getToken({ 'name': name }, TOKEN_SECRET, TOKEN_ALGORITHM )
        return jsonify(
            getSuccessForm('로그인에 성공하셨습니다.', {
                'name': name,
                'password': '비공개',
                'accessToken': token
            })
        )
    else:
        return jsonify(
            getFailureForm('로그인에 실패하셨습니다.')
        )

#선택창 이름 불러오기
@app.route('/nespresso', methods=['GET'])
def show_nespresso():
    name = request.args.get('name')
    return render_template('./pages/select.html', title='캡슐커피 취향저격', name=name)

#index 창
@app.route("/")
def main():
    img='https://www.nespresso.com/shared_res/mos/free_html/kr/images/Voltesso-Mobile.jpg'
    return render_template("/pages/index.html",img=img)

if __name__ == '__main__':

    app.run(
        '0.0.0.0',
        port=PORT,
        debug=True)