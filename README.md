# intract2019
intract 2019 登壇準備資料

master: 本番用
practice: ライブコーディング練習用ブランチ


## 作業順

1. [2min] ゴールの説明(スライド)
1. [1min] 自己紹介
1. [2min] 構築までの道のり～レシピ手順一覧(スライド) 
1. [10min] webapps for linux 構築(Azureポータル)
1. [5min] Flaskの説明(スライド)
1. [5min] プロジェクトの作成(PyCharm)
1. [5min] APIの作成(PyCharm)
1. [5min] API URLの動的生成(PyCharm)
1. [5min] Jinja2を使ったhtmlテンプレートの作成(PyCharm)
1. [10min] Github連携
1. コミット＆プッシュ
1. web公開されてますように・・・・
1. [3min] まとめ


## イベント前に準備しておくこと
- Gitリポジトリの作成（このリポジトリ）
- resource groupの作成
- venv
- PyCharmのオープン（本リポジトリオープン）


## Webapps 作成


## Flask-1
- requirements.txt の説明 -> パッケージ管理ツール・モジュール管理ツール
    - Java : Maven/ Gradle
    - Node : package.json
```
Flask==1.0.3
```

- application.py を新規作成 -> application.pyの名前指定ポイント説明

```python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

```

- run
    - PyCharmコミュニティエディションはFlask対応していません。Flask開発を幸せにやるならPyCharm有料版をお買い求めください！
    - VSCodeやPyCharmコミュニティエディションでもできないことはないです↓だいじょうぶ。
    ```bash
      export FLASK_APP=application.py
      flask run
    ```
    - [http://localhost:5000/](http://localhost:5000/)
    - windowsの場合(コマンドライン)
    ```python
      set FLASK_APP=application.py
      flask run
    ```

- ページルーティング
```python
@app.route('/greeting/jp')
def greeting():
    return 'こんにちは！'
```

```python
@app.route('/greeting/<string:user_name>')
def greeting_user(user_name):
    return '{uname}さん、さようなら！'.format(uname=user_name)
```

```python
from flask import request

@app.route('/greeting')
def greeting_name():
    user = request.args.get('user')
    return '{uname}さん、疲れてる？'.format(uname=user)
```

- run
    - http://localhost:5000/
    - http://localhost:5000/greeting/jp
    - http://localhost:5000/greeting/まーや
    - http://localhost:5000/greeting?user=まーや（参加者に名前聞いてもいい）
    
- jinja2
    - templatesディレクトリの作成
    - index.htmlの作成
```html
<title>welcome!</title>

<h1>Welcome! {{name}}さん!</h1>
```

```python
import flask

@app.route('/welcome/<string:user_name>')
def welcome_index(user_name):
    return flask.render_template(
        'index.html',
        name=user_name
    )
```

- run
    - http://localhost:5000/welcome/まーや

## git連携
gitデプロイが開始したら下記説明＆時間つぶし

- ログの閲覧方法
- Azure devops
- flask-2 (post form)

リリース完了後

- /
- /hello/jp
- /greeting/まーや
- /greeting?user=まーや（参加者に名前聞いてもいい）
- /welcome/まーや

## flask-2

- post form
    - index.htmlをコピー -> echo.html
    ```html
      <title>welcome!</title>
        
      <p>あなたの打った文字</p>
      <h1>{{echo}}</h1>
    ```
    - index.htmlに追加
    ```html
      <form action="/echo" method="POST">
        <input type="text" name="input_word" />
        <button type="submit">GO!</button>
      </form>
    ```
    - apiの追加
   ```python
      @app.route('/echo', methods=['POST'])
      def echo():
          echo_word = request.form['input_word']
          return flask.render_template(
              'echo.html',
              echo=echo_word
          )
    ```
 
 ## 再プッシュ＆確認
 
 ## まとめ
