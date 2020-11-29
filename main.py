from flask import Flask
import requests

app = Flask(__name__)

@app.route(/)
def top():
    return "郵便番号(半角数字7桁)をもとに住所を検索します。" \
           "ハイフンなしで入力してください。"
    # 郵便番号を取得
    zcode = str(input())

@approute("/address_search?zipcode=<zcode>")
def getzcode():
    # 郵便番号をもとに情報を取得
    url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=" + zcode
    res = requests.get(url)
    resinfo = res.json()

    # 住所を抽出し値を戻す
    for info in resinfo["results"]:
        address = info["address1"] + info["address2"] + info["address3"]

    return address