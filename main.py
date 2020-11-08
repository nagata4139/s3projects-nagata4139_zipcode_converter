import csv
import requests

# CSVファイルの作成と初期化
cfile = open("output.csv", "w")
cfile.truncate(0)
cfile.close()

# テキストファイルを読み込み1行ずつ処理
with open("zipcodes.txt","r",encoding="utf_8") as ztxt:
    zlist = ztxt.readlines()

    # 郵便番号をもとに情報を取得
    for zcode in zlist:
        zcode = zcode.replace("\n", "")
        url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=" + zcode
        res = requests.get(url)
        resinfo = res.json()

        # 住所を抽出
        for info in resinfo["results"]:
            address = info["address1"] + info["address2"] + info["address3"]

        # 郵便番号と住所をCSVに書込み
        with open("output.csv","a",newline = "") as cfile:
            cline = csv.writer(cfile)
            cline.writerow([zcode,address])