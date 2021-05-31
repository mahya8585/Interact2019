# Win10+VSCode版：WebApps+Flask チュートリアル的デモ

## 作業順

1. ゴールの説明(スライド)
1. 構築までの道のり～レシピ手順一覧(スライド) 
1. Web Apps for linux 構築(Azureポータル)
1. Flaskの説明(スライド)
1. プロジェクトの作成(VSCode)
1. APIの作成(VSCode)
1. API URLの動的生成(VSCode)
1. Jinja2を使ったhtmlテンプレートの作成(VSCode)
1. GitHub - Web Appsをデプロイセンターから連携
1. コミット＆プッシュ
1. web公開されてますように・・・・
1. まとめ


## 事前準備しておいたこと
- VSCode
  - extentions
  - pyランチャーバージョンの設定
- ブラウザ


## Webapps 作成

今回は後続の機能説明のためS1を作成。自分にあったプランを選びましょう〜    
ちなみにVSCode上からもExtentionsいれれば作成できるし、CLI使ってコマンドラインから作成もできる。   
が今回はAzureのポータル画面を見ていただきたいのであえてAzureポータルから作業します

## VSCodeの準備
- Extentions
  - https://marketplace.visualstudio.com/items?itemName=KnisterPeter.vscode-github
  - https://marketplace.visualstudio.com/items?itemName=ms-python.python

## Flask
- requirements.txt の作成

```
Flask==2.0.1
```
- pip
```
(Windows&複数バージョン保持&最新バージョンへのpip)
py -m pip install -r requirements.txt
```

- application.py を新規作成 -> 簡単にWeb Apps for Linuxで動かしたいならルーティングファイルの名前は「application.py」にすること
  - 実行ファイル名を変更することも可能です(WebApps構築後WebApps内のconfigファイルを変更すれば)

```python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'
    
    
if __name__ == "__main__":
    app.run()

```

- run
    - VSCodeでももちろんできるよ
    ```bash
      (Mac)
      export FLASK_APP=application.py
      flask run
      
      もしくは右クリックでRun Python file in Terminal
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
    @app.route('/profile/<string:user_name>')
    def user_profile(user_name):
        return '{name}さんのプロフィール画面です'.format(name=user_name)
    ```

    - ゲットパラメータ(おまけ)
    ```python
    from flask import request

    @app.route('/profile')
    def greeting_name():
        user = request.args.get('user')
        return '{uname}さんのプロフィール画面です(クエリパラメータ版)'.format(uname=user)
    ```
    - jinja2の利用例(おまけ)
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
    - http://localhost:5000/
    - http://localhost:5000/profile/maaya
    - http://localhost:5000/profile?user=まーや  (おまけ)
    - http://localhost:5000/welcome/maaya    (おまけ)
    

## GitHubへプッシュ from VSCode
- publish GitHub
- publish対象のファイルを選択
- (GitHubログイン)
- プッシュされたらGitHub上での表示確認

    
## git連携
- デプロイセンター設定する
    - 最近Newデプロイセンターになりました(GitHubはGitHub Actionsに)
      - 設定を作る -> 保存 -> デプロイ実行されるよ
    - ログの閲覧方法
    - Azure devops  (おまけ)
- 完了チェック
    - /
    - /profile/maaya
    - /profile?user=maaya
    - /welcome/maaya

 
 ## まとめ

## tips
- Azure Monitor
- CORS設定
- SSH接続
- Azure DevOps / GitHub Actions
- Azure pipeline
- slotデプロイ
- App Insight


