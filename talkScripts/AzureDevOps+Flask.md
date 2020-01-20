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

- (コミット・プッシュ)

- 「DevOps reposと連携する」をDoneに移動する


### DevOps pipeline

- 「DevOps pipeline」をdoingに移動する
- とりあえずyamlの設定を何も変更せずに実行する
  - CDパイプライン完成

- テスト実行する
  - 下記をyamlに追加
  ```python
  ```
  - Tox testでテストの並列実行も可能な旨をコメント

- 「DevOps pipeline」をDoneに移動する


### プルリク

- 「プルリクを投げる」をDoingに移動する
  
- (プルリクを投げる)
- (レビューしてもらう)
- (マージしてもらう)
- (pipelineの動きを確認する)

- 「プルリクを投げる」をDoneに移動する
