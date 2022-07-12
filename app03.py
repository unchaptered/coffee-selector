from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.dvsntob.mongodb.net/cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/nespresso/hard')
def home():
    return render_template('index03.html')

@app.route('/nespresso/hard/time')
def nespresso():
    return render_template('index04.html')


@app.route('/nespresso/hard', methods=['GET'])
def show_nespresso():
    hard_receive = request.args.get('hard_give')
    soft_receive = request.args.get('soft_give')


@app.route('/nespresso/hard', methods=['POST'])
def save_nespresso():
    hard_receive = request.form['hard_give']
    soft_receive = request.form['soft_give']


    doc = {
        'hard':hard_receive,
        'soft':soft_receive
    }
    db.nespresso.insert_one(doc)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug=True)