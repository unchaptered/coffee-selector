from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
load_dotenv()

import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='캡슐커피 취향저격')

if __name__ == '__main__':
    app.run(
        '0.0.0.0',
        port=os.environ.get('port'),
        debug=True)