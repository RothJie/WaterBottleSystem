import json
import random
import datetime
import requests
import time


# print(str(int(time.time()*1000)))
# print(datetime.datetime.today().strftime('%Y%m%d'))

f0 = open(file='User_Agent_li.txt', mode='r', encoding='utf-8')
u_a_li = eval(f0.read())


def getFull(code, date):
    url_ = 'http://push2ex.eastmoney.com/getStockChanges'

    data = {
        "cb": f"jQuery35107738871601504242_1685{random.randint(99999,999999)}524",
        "ut": "7eea3edcaed734bea9cbfc24409ed989",
        "date": f"{date}",
        "dpt": "wzchanges",
        "code": f"{code}",
        "market": f"{0 if code[0] == '0' else 1}",
        "_": f"{int(time.time() * 1000)}"
    }
    headers = {
        "User-Agent": random.choice(u_a_li)
    }
    resp = requests.get(url=url_, data=data, headers=headers)
    get_data = json.loads(str(resp.text).strip().strip("jQuery35107738871601504242_1685238871524(").strip(");"))["data"]

    with open("info1.json", mode="r", encoding="utf-8") as f:
        info = json.load(f)

    buy = 0
    sell = 0
    for uni in get_data["data"]:
        if str(uni['t']) in info[3]:
            buy += uni['v']
        if str(uni['t']) in info[2]:
            sell += uni['v']
        print(uni)
    print(buy / (buy + sell), sell / (buy + sell))


if __name__ == '__main__':
    # code = str(input("请输入股票代码:"))
    code = "600332"
    date = 20230526
    getFull(code, date)
