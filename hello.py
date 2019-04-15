from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hi world!!"

@app.route('/sing')
def sing():
    return "sing jaaaaaaaaaaaaaaaaaa"

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        return "eiei 1.."
    elif request.method == 'GET':
        return "eiei 2.."
