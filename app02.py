from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.dvsntob.mongodb.net/cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/nespresso')
def home():
    return render_template('index02.html')

@app.route('/nespresso/hard')
def nespresso():
    return render_template('index03.html')


@app.route('/nespresso', methods=['GET'])
def show_nespresso():
    red_receive = request.args.get('red_give')
    green_receive = request.args.get('green_give')

@app.route('/api/nespresso', methods=['POST'])
def save_nespresso():
    chocolate_receive = request.form['chocolate_give']
    biscuit_receive = request.form['biscuit_give']

    doc = {"chocolate": chocolate_receive,
           "lemon": lemon_receive}
    db.words.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '다음 선택!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug=True)