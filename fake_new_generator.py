import requests 
import json
import os

__author__ = 'hwpoison'

session = requests.Session()

def post_request(url, payload, headers={'Content-type': 'application/json'}):
    try:
        req = session.post(url, data=json.dumps(payload), verify=True, headers=headers)
        req.raise_for_status()
        return json.loads(req.text)
    except requests.exceptions.RequestException as err:
        print("Oops!:", err)
        return False

def fakenew_generator(content, length=10000):
    api_news_url = "https://wudao.aminer.cn/api/xinhua/"
    data = {
        "content":content,
        "max_length":length
    }
    out = post_request(api_news_url, data)
    if out:
        return out["result"]
    else:
        return "Error."

while True:
    inpt = input("Input:")
    out = fakenew_generator(inpt)
    if out:
        print("Out:", out)
    print("="*50)

