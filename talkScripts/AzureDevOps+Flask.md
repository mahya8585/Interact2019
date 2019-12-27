# Azure DevOps + WebApps + Flask

## 事前準備しておいたもの(★説明するもの)

- ★Gitリポジトリの作成（このリポジトリ）
- ★resource groupの作成
- ★Azure DevOpsプロジェクト
  - やることリストチケット付き
  - repo イニシャルコミット済
    - readme.mdだけ作成しておく
  - ローカルクローン済み
- venv
- PyCharm
- ブラウザ

## Azure DevOpsBoad

- (すでに今日やるデモチケットが起票されている)
- 「事前準備しておいたものたちの説明」をDoing/Done
- 「Azure WebAppsを作成する」をDoing
- 「Demo用Webシステムを作成する」Doing

## Webapps 作成

とりあえずdemoなのでB1で作成します。    
自分にあったプランを選びましょう～    

## Flask

- requirements.txt の作成

```python
Flask==1.0.3
```

- application.py を新規作成 -> 簡単にWeb Apps for Linuxで動かしたいならルーティングファイルの名前は「application.py」にすること

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
    - http://localhost:5000/

- WebApps作成完了確認
  - ドメインリクエストチェック
- チケットをDoneへ移動する
  - 「Azure WebAppsを作成する」
  - 「Demo用Webシステムを作成する」

## Azure DevOps連携

### Repos

【TBD】

- (ブランチ作成)
- (コミット・プッシュ)

- 「DevOps reposと連携する」をDoneに移動する

### testplans

- 「Azure test plans」をDoingに変更する

【TBD】

- 「Azure test plans」をDoneに変更する

### テストコード作成

- 「テストコードを書く」をDoingに移動する

【TBD】

- (コミット・プッシュ)

- 「テストコードを書く」をDoneに移動する

### プルリク

- 「プルリクを投げる」ｗDoingに移動する
  
【TBD】

- (プルリクを投げる)
- (レビューしてもらう)
- (マージしてもらう)
- (testplansの動きを確認する)

- 「プルリクを投げる」をDoneに移動する

### DevOps pipeline

- 「DevOps pipeline」をdoingに移動する

【TBD】

- 承認つきCD

- 「DevOps pipeline」をDoneに移動する
  
### 追加コーディング

```python
@app.route('/greeting/<string:user_name>')
def greeting_user(user_name):
    return user_name + 'さん、こんばんは！'
```

- http://localhost:5000/greeting/maaya

- DevOps　CI/CD 実行


