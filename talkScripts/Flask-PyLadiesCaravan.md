## Hello world

- new project
- pip install flask
- create new file > application.py

## Hello API

```python
import flask
app = flask.Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'
    
    
if __name__ == '_main__':
    app.run()
```

- intelliJ run
- windows
  - set FLASK_APP=app.py
  - flask run
- mac
  - export FLASK_APP=app.py
  - flask run
    
    
- http://localhost:5000/

### routing(動的パラメータ)

```python
@app.route('/hello/<string:user_name>')
def hello_user(user_name):
    return '{uname}さん、こんちわ！'.format(uname=user_name)
```

- http://localhost:5000/
- http://localhost:5000/hello/maaya

### routing(GETパラメータ)

```python
@app.route('/greeting')
def greeting():
    user = flask.request.args.get('user')
    display = 'やぁやぁ! ' + user
    return flask.render_template_string(display)
```

- http://localhost:5000/greeting?user=まーや

## Hello Jinja2

- templatesディレクトリの作成
- index.htmlの作成
```html
  <title>welcome!</title>
  <h1>Welcome! {{name}}さん!</h1>
```
    
    
- ルーティング
```python
@app.route('/welcome/<string:user_name>')
def welcome_index(user_name):
    return flask.render_template(
        'index.html',
        name=user_name
    )
```

- http://localhost:5000/welcome/maaya

### post form

- echo.htmlの作成
```html
<p>あなたの打った文字はこちら</p>
<h1>{{echo}}</h1>
```

- index.htmlに追加
```html
  <form action="/echo" method="POST">
    <input type="text" name="input_word" />
    <button type="submit">GO!</button>
  </form>
```

- ルーティング
```python
@app.route('/echo', methods=['POST'])
   def echo():
       echo_word = flask.request.form['input_word']
       return flask.render_template(
           'echo.html',
           echo=echo_word
       )
```

- http://localhost:5000/welcome/まーや

## Hello injection

- run
    - http://localhost:5000/greeting?user=まーや
    - http://localhost:5000/greeting?user=<script>alert("hack")</script>
    
- コード変更
    - display = 'こんにちは! ' + flask.escape(user)

- run 
    -  http://localhost:5000/greeting?user=<script>alert("hack")</script>
    -  
