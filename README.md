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

## Webapps 作成


## Flask

- requirements.txt の説明
- application.py を新規作成

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

```

- run
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
@app.route('/greeting')
def greeting():
    return 'こんにちは！'
```

```python
@app.route('/greeting')
def greeting_name(user_name):
    return '{uname}さん、疲れてる？'.format(uname=user_name)
```

```python
@app.route('/greeting/<string:user_name>')
def greeting_user(user_name):
    return '{uname}さん、さようなら！'.format(uname=user_name)
```

- run

- 