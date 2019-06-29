from flask import Flask
from flask import request
import flask
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


@app.route('/welcome/<string:user_name>')
def index(user_name):
    return flask.render_template(
        'index.html',
        name=user_name
    )


@app.route('/echo', methods=['POST'])
def echo():
    echo_word = request.form['input_word']
    return flask.render_template(
        'echo.html',
        echo=echo_word
    )
