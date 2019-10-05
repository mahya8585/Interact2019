# intract2019
intract 2019 登壇準備資料

master: 本番用
practice: ライブコーディング練習用ブランチ

# 当日叩いたコマンドやコード

## 作業順

1. ゴールの説明(スライド)
1. 自己紹介
1. 構築までの道のり～レシピ手順一覧(スライド) 
1. Web Apps for linux 構築(Azureポータル)
1. Flaskの説明(スライド)
1. プロジェクトの作成(PyCharm)
1. APIの作成(PyCharm)
1. API URLの動的生成(PyCharm)
1. Jinja2を使ったhtmlテンプレートの作成(PyCharm)
1. GitHub - Web Appsをデプロイセンターから連携
1. コミット＆プッシュ
1. web公開されてますように・・・・
1. まとめ


## 事前準備しておいたこと
- Gitリポジトリの作成（このリポジトリ）
- resource groupの作成
- venv
- PyCharm
    - PyCharmコミュニティエディションはFlask対応していません。Flask開発を幸せにやるならPyCharm有料版をお買い求めください！
- ブラウザ


## Webapps 作成

B1を作成しました。自分にあったプランを選びましょう〜

## Flask
- requirements.txt の作成

```
Flask==1.0.3
```

- application.py を新規作成 -> 簡単にWeb Apps for Linuxで動かしたいならルーティングファイルの名前は「application.py」にすること

```python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

```

- run
    - VSCodeでももちろんできるよ
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
    - 動的URL
    ```python
    @app.route('/greeting/<string:user_name>')
    def greeting_user(user_name):
        return '{uname}さん、こんばんは！'.format(uname=user_name)
    ```

    - ゲットパラメータ
    ```python
    from flask import request

    @app.route('/greeting')
    def greeting_name():
        user = request.args.get('user')
        return '{uname}さん、おはよう？'.format(uname=user)
    ```

- run
    - http://localhost:5000/
    - http://localhost:5000/greeting/maaya
    - http://localhost:5000/greeting?user=まーや
    
## git連携
- デプロイセンター設定する
    - ログの閲覧方法
    - Azure devops
- 完了チェック
    - /
    - /greeting/maaya
    - /greeting?user=maaya
    - /welcome/maaya

## flask-2
- jinja2の利用例
    - templatesディレクトリの作成
    - index.htmlの作成
    ```html
    <title>welcome!</title>
    <h1>Welcome! {{name}}さん!</h1>
    ```
    - ルーティング
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
    - http://localhost:5000/welcome/maaya

- post form
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

- run
    - http://localhost:5000/welcome/まーや
    
## インジェクション
@app.route('/hello')
def hello_injection():
    name = flask.request.args.get('name')
    hello_b = 'hello ' + name
    return flask.render_template_string(hello_b)
    
 - http://localhost:5000/hello?name=maaya
 - http://localhost:5000/hello?name=<script>alert("hack")</script>
 
 name_esc = flask.escape(name)
 
 - http://localhost:5000/hello?name=<script>alert("hack")</script>
 
 ## まとめ

## そのあとした雑談
- Azure Monitor
- CORS設定
- SSH接続
- Azure DevOps
- Azure pipeline
- slotデプロイ
- App Insight


