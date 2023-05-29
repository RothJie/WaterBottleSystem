import json
import random
import datetime
import requests
import time


f0 = open(file='User_Agent_li.txt', mode='r', encoding='utf-8')
u_a_li = eval(f0.read())


url_ = 'http://push2ex.eastmoney.com/getAllStockChanges?'

data = {
    # "type": "64,256,8193,8201,8202",  # 有大买盘、机构买单、大笔买入、火箭发射、快速反弹
    "type": "8201",  # 有大买盘、机构买单、大笔买入、火箭发射、快速反弹
    "cb": f"jQuery351023688794158570503_168527{random.randint(99999,999999)}4",
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
sto_data = json.loads(str(resp.text).strip().strip('jQuery351023688794158570503_1685272332240(').strip(');'))["data"]['allstock']

data_10 = sto_data[:10]


def JudgeMarket(code: str):
    if code[0] == '0':
        return 'sz'
    elif code[0] == '3':
        return 'sz'
    elif code[0] == '6':
        return 'sh'
    elif code[0] == '8':
        return 'bj'


def JudgeChangeType(types_code: str):
    with open(file='info1.json', mode='r', encoding='utf-8') as f:
        type_data = json.load(f)
        for types_ in type_data[0].items():   # ('有大卖盘', '128')
            if types_[1] == types_code:
                return types_[0]


def HangQing_url():
    for uni in data_10:
        ind = data_10.index(uni) + 1
        time_ = str(uni['tm'])
        code = str(uni['c'])
        name = uni['n']
        types_code = str(uni['t'])
        type_ = JudgeChangeType(types_code)
        stock_info_url = JudgeMarket(code) + code
        ttm = ''
        for i in range(len(time_)):
            if i % 2 == 0 and i != 0:
                ttm += ":"
            ttm += time_[i]

        if JudgeMarket(code) != 'bj':
            print(f"第{ind} 时间：{ttm} 代码：{code} 名称：{name} 异动类型：{type_} \n详情页:http://quote.eastmoney.com/{stock_info_url}.html#fullScreenChart")
        else:
            print(f'第{ind} 时间：{ttm} 代码：{code} 名称：{name} 异动类型：{type_} \n详情页:https://so.eastmoney.com/web/s?keyword={code}')


if __name__ == '__main__':
    HangQing_url()
    """
    tm  时间
    c   代码
    m   不明确
    n   名称
    t   异动类型代码
    i   详细信息（不同类型有不同含义）
    """

