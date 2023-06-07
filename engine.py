import random
import pymysql
import requests
import time
import json


def engine(type_: str = "火箭发射"):
    f0 = open(file='User_Agent_li.txt', mode='r', encoding='utf-8')
    u_a_li = eval(f0.read())

    url_ = 'http://push2ex.eastmoney.com/getAllStockChanges?'

    types = ["64", "8193", "8201", "8202", "8207"]
    types_zh = ["有大买盘", "大笔买入", "火箭发射", "快速反弹", "竞价上涨"]

    data = {
        # "type": "64,256,8193,8201,8202",  # 有大买盘、机构买单、大笔买入、火箭发射、快速反弹
        "type": f"{types[types_zh.index(type_)]}",  # 有大买盘64、机构买单256、大笔买入8193、火箭发射8201、快速反弹8202
        "cb": f"jQuery351023688794158570503_168527{random.randint(99999, 999999)}4",
        "ut": "7eea3edcaed734bea9cbfc24409ed989",
        "pageindex": "0",
        "pagesize": "30",
        "dpt": "wzchanges",
        "_": f"{int(time.time() * 1000)}"
    }

    headers = {
        "User-Agent": random.choice(u_a_li)
    }

    resp = requests.get(url=url_, data=data, headers=headers)
    sto_data = \
        json.loads(str(resp.text).strip().strip('jQuery351023688794158570503_1685272332240(').strip(');'))["data"][
            'allstock']

    data_10 = sto_data[:10]
    return data_10


def judgeMarket(code: str):
    if code[0] == '0':
        return 'sz'
    elif code[0] == '3':
        return 'sz'
    elif code[0] == '6':
        return 'sh'
    elif code[0] == '8':
        return 'bj'


def judgeChangeType(types_code: str):
    with open(file='info1.json', mode='r', encoding='utf-8') as f:
        type_data = json.load(f)
        for types_ in type_data[0].items():  # ('有大卖盘', '128')
            if types_[1] == types_code:
                return types_[0]


def hangQingUrl(type_: str = "火箭发射"):
    data_10 = engine(type_)
    contents = dict()
    params = []
    for uni in data_10:
        ind = data_10.index(uni) + 1
        time_ = str(uni['tm'])
        code = str(uni['c'])
        name = uni['n']
        types_code = str(uni['t'])
        type_ = judgeChangeType(types_code)
        stock_info_url = judgeMarket(code) + code
        ttm = ''
        for i in range(len(time_)):
            if i % 2 == 0 and i != 0:
                ttm += ":"
            ttm += time_[i]
        if judgeMarket(code) != 'bj':
            url_str = f'http://quote.eastmoney.com/{stock_info_url}.html#fullScreenChart'
            base_info = f'第{ind}个 时间：{ttm} 名称：{name} 异动类型：{type_}'
            contents[f"{code}"] = [url_str, base_info]
        else:
            url_str = f'https://so.eastmoney.com/web/s?keyword={code}'
            base_info = f'第{ind}个 时间：{ttm} 名称：{name} 异动类型：{type_}'
            contents[f"{code}"] = [url_str, base_info]
        params.append((code, name, ttm))
    return contents, params


def dataToMysql(params: list, sql: str):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='abc123')
    cursor = conn.cursor()
    cursor.execute('use morning_fifteen_minutes;')
    for param in params:
        param = param
        cursor.execute(sql, param)
        conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    cont = hangQingUrl("火箭发射")[0]
    cont1 = hangQingUrl("火箭发射")[1]
    dataToMysql(sql='insert into rocket values(%s,%s,%s);', params=cont1)
