from flask import Flask
from flask import request
import flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/greeting/jp')
def greeting():
    return 'こんちは！'


@app.route('/greeting/<string:user_name>')
def greeting_user(user_name):
    return '{uname}さん、さようなら！'.format(uname=user_name)


@app.route('/greeting')
def greeting_name():
    user = request.args.get('user')
    return '{uname}さん、疲れてる？'.format(uname=user)


@app.route('/welcome/<string:user_name>')
def welcome_index(user_name):
    return flask.render_template(
        'index.html',
        name=user_name
    )

