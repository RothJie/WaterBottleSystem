import json
import re

with open("info1.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)
    print(list(dict(data[0]).values()))
    print(list(dict(data[1]).values()))




