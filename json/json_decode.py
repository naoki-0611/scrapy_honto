import json


# str = '''[
# {"title": "<title>\u6f2b\u753b\u30fb\u30b3\u30df\u30c3\u30af\u30e9\u30f3\u30ad\u30f3\u30b0 - honto</title>"},
# {"title": "<title>\u6f2b\u753b\u30fb\u30b3\u30df\u30c3\u30af\u30e9\u30f3\u30ad\u30f3\u30b0 - honto</title>"}
# ]'''


with open("../scrapy_honto/spiders/test.json")as f:
    df = json.load(f)
    print(df)

