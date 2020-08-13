# automatic_transaction
## 概要
OANDAのAPIを用いてFX自動売買を行う。
今後ロジックを追加していく。

## 必要なもの
Python 3.7.4
Flask 1.1.1
Werkzeug 0.16.0

## セットアップ方法
```
# 環境変数の設定
cp env.development .env

# 関連パッケージのインストール
pipenv install

# DBの初期化
pipenv run python manage.py init_db
```

## サーバ起動
```
 # 環境変数読み込み
 source .env

 # サーバ起動
 python3 server.py
```

## デプロイ
```
# Herokuへデプロイ
git push heroku master 
```

## テスト
```
# テストの実行
coverage run -m unittest

# テストカバレッジ計測
coverage report -m

# テストカバレッジレポート作成
coverage html
```

## 購入ロジックの追加
app/services/order_price_manager.pyを変更する。
