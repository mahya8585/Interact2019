from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world!'


@app.route('/greeting/<string:user_name>')
def greeting_usr(user_name):
    return '{uname}さん、こんばんは！'.format(uname=user_name)


@app.route('/greeting')
def greeting_name():
    user = request.args.get('user')
    return '{uname}さん、おはよう？'.format(uname=user)
