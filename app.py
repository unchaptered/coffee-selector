from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import json
from modules.env import PORT, MONGO_URL, DATABASE_NAME, COLLECTION_USER, COLLECTION_CAPSULE
from modules.database import getMongoClient
from modules.form import getSuccessForm, getFailureForm

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.dvsntob.mongodb.net/cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nespresso')
def nespresso():
    return render_template('index02.html')


@app.route('/nespresso', methods=['GET'])
def show_nespresso():
    chocolate_receive = request.args.get('chocolate_give')
    biscuit_receive = request.args.get('biscuit_give')
    lemon_receive = request.args.get('lemon_give')

@app.route('/api/nespresso', methods=['POST'])
def save_nespresso():
    chocolate_receive = request.form['chocolate_give']
    biscuit_receive = request.form['biscuit_give']
    lemon_receive = request.form['lemon_give']
    doc = {"chocolate": chocolate_receive,
           "biscuit": biscuit_receive,
           "lemon": lemon_receive}
    db.words.insert_one(doc)
    return jsonify({'result': 'success'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug=True)