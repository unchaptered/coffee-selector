from flask import Flask, render_template, request, jsonify
from env import port

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='캡슐커피 취향저격')

if __name__ == '__main__':
    app.run(
        '0.0.0.0',
        port=port,
        debug=True)