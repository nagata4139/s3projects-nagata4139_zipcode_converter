import requests

# 郵便番号を取得
zcode = str(input("郵便番号を入力してください。"))

# 郵便番号をもとに情報を取得し出力
zcode
url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=" + zcode
res = requests.get(url)
resinfo = res.json()
print(resinfo)