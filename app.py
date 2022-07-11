from flask import Flask, render_template, request, jsonify
from env import port
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
app = Flask(__name__)

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


if __name__ == '__main__':

    app.run(
        '0.0.0.0',
        port=port,
        debug=True)