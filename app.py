from flask import Flask, redirect, render_template, request, jsonify, url_for

# Provider : 특정 기능을 공급하는 함수들
from database import getUser, getSelect, getCapsule
from src.modules.provider.form_provider import getSuccessForm, getFailureForm
from src.modules.config.config_provider import PORT, TOKEN_SECRET, TOKEN_ALGORITHM

# Validator : 특정 값의 유효성을 테스트하는 함수들
from src.modules.vadliator.form_validator import validate_name, validate_password
# Tokenizer : 토큰을 생성하는 함수
from src.modules.auth.tokenizer import getToken
# from src.modules.auth.bcrypt import compareHashPw, getBcrypt, getHashPw

app = Flask(__name__)
# bcrypt = getBcrypt(app)

@app.route("/")
def main():
    img = 'https://www.nespresso.com/shared_res/mos/free_html/kr/images/Voltesso-Mobile.jpg'
    return render_template("/pages/index.html", img=img)

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

# 선택창 이름 불러오기
@app.route('/nespresso', methods=['GET'])
def show_nespresso():
    name = request.args.get('name')
    return render_template('./pages/select.html', title='캡슐커피 취향저격', name=name)

# 선택창 select에 임시저장
@app.route('/nespresso', methods=['POST'])
def save_nespresso():
    name=request.form['name']
    doc = {
        'user_name': name,
        'cake':int( request.form['cake_give']),
        'apple': int(request.form['apple_give']),
        'strength': int(request.form['strength_give']),
        'milk': int(request.form['milk_give']),
        'size': int(request.form['size_give'])
    }
    if getSelect().find_one({'user_name': name}) is not None:
        getSelect().delete_one({'user_name': name})
        getSelect().insert_one(doc)
    else:
        getSelect().insert_one(doc)
    return jsonify({'msg': '선택 완료!'})

# 결과창
@app.route('/result', methods=["GET"])
def result_list():
    user_name = request.args.get('name')
    doc = getSelect().find_one({'user_name': user_name})
    print(doc)
    root1=list(getCapsule().find({},{"_id":False}))
    if doc['strength'] == 1:
        count=0
        while True:
            for i in root1:
                if i['tasty']['strong']<=7:
                    count+=1
                    root1.remove(i)
            if count==0:
                break
            count=0
    else:
        count = 0
        while True:
            for i in root1:
                if i['tasty']['strong'] > 7:
                    count += 1
                    root1.remove(i)
            if count == 0:
                break
            count = 0

    if doc['milk'] == 0:
        count = 0
        while True:
            for i in root1:
                if i['tasty']['bitter'] >2:
                    count += 1
                    root1.remove(i)
            if count == 0:
                break
            count = 0
    else:
        count = 0
        while True:
            for i in root1:
                if i['tasty']['bitter'] <= 2:
                    count += 1
                    root1.remove(i)
            if count == 0:
                break
            count = 0
    return render_template('/pages/result.html',list=root1, title='캡슐커피 취향저격', user_name=user_name)

@app.route('/api/result', methods=["POST"])
def saver_cof():
    cof_name = request.form['cof_name']
    user_name = request.form['user_name']
    print(cof_name, user_name)
    getSelect().delete_one({'user_name': user_name})
    doc={
        'user_name': user_name,
        'cof_name': cof_name
    }
    getSelect().insert_one(doc)
    return jsonify(
        getSuccessForm('기록성공', {
            'name': user_name,
            'cof_name': cof_name,
        })
    )

@app.route('/api/join', methods=['POST'])
def api_join():

    name = validate_name(request.form['name'])
    password = validate_password(request.form['password'])
    
    if name is None or password is None:
        return jsonify(
            getFailureForm('텅빈 이름/비밀번호를 전달 받았습니다.', {
                'name': name,
                'password': password
            })
        )

    # 중복 검사
    find = getUser().find_one({
        'name': name
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
            'password': password
            # 'password': getHashPw(bcrypt, password)
        })

        # 이미 중복된 사용자가 없는 경우 -> 회원가입 성공
        return jsonify(
            getSuccessForm('회원가입에 성공하셨습니다.', {
                'name': name,
                'password': '비공개'
            })
        );

@app.route('/api/login', methods=['POST'])
def api_login():

    name = validate_name(request.form['name'])
    password = validate_password(request.form['password'])

    if name is None or password is None:
        return jsonify(
            getFailureForm('유효하지 않는 가입을 전달 받았습니다.')
        )

    is_exists = getUser().find_one({
        'name': name
    })
    if is_exists is None:
        return jsonify(getFailureForm('존재하지 않는 이름을 전달 받았습니다.'))

    # compared = compareHashPw(
    #     bcrypt,
    #     is_exists['password'],
    #     password
    # )

    if is_exists['password'] == password is False:
        return jsonify(getFailureForm('일치하지 않는 비밀번호를 전달 받았습니다.'))

    else:
        token = getToken({ 'name': name }, TOKEN_SECRET, TOKEN_ALGORITHM )
        return jsonify(
            getSuccessForm('로그인에 성공하셨습니다.', {
                'name': name,
                'password': '비공개',
                'accessToken': token
            })
        )

@app.route('/api/get_reviews', methods=['GET'])
def get_reviews():
    review_receive = request.args.get("review_give")
    result = list(db.reviews.find({"review": review_receive}, {'_id': 0}))

    return jsonify({'result': 'success', 'reviews': result})


@app.route('/api/save_review', methods=['POST'])
def save_review():
    review_receive = request.form['review_give']
    doc = {"review": review_receive}
    getSelect().reviews.insert_one(doc)
    return jsonify({'result': 'success', 'msg': f'review"{review_receive}" saved'})


@app.route('/api/delete_review', methods=['POST'])
def delete_review():
    review_receive = request.form['review_give']
    number_receive = int(request.form["number_give"])
    review = list(getSelect().reviews.find({"review": review_receive}))[number_receive]["review"]
    print(review_receive, review)
    getSelect().reviews.delete_one({"review": review})
    return jsonify({'result': 'success', 'msg': f'review #{number_receive} of "{review_receive}" deleted'})

if __name__ == '__main__':
    app.run(
        '0.0.0.0',
        port=PORT,
        debug=True)
