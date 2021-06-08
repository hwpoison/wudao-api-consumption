import requests 
import json
import os

__author__ = 'hwpoison'

session = requests.Session()

API_CLIENT_ID = ""
API_SECRET_KEY = ""

def post_request(url, payload, headers={'Content-type': 'application/json'}):
    try:
        req = session.post(url, data=json.dumps(payload), verify=True, headers=headers)
        req.raise_for_status()
        return json.loads(req.text)
    except requests.exceptions.RequestException as err:
        print("Oops!:", err)
        return False

def getBaaiApiToken():
    auth_url = "https://wudaoai.cn/model-api/api/v1/auth"
    auth_data = {
        "clientId":API_CLIENT_ID,
        "secretKey":API_SECRET_KEY    
    }
    req = post_request(auth_url, auth_data)
    return req['data']['apiToken']

def vectorText(text):
    token = getBaaiApiToken() 
    data = {
        'file':'',
        'baaiApiToken':token,
        'json':{"text":text}
    }
    api_txtvect = "https://wudaoai.cn/model-api/api/v1/verifyApi"
    req = post_request(api_txtvect, data, {'Content-type':'form-data'})
    return req['data']

def poems_generator(content):
    # input format : <title>&&<author>&&<poem_text>
    api_poems_url = "https://wudao.aminer.cn/api/fastpoem/"
    data = {
        'content':content
    }
    out = post_request(api_poems_url, data)
    if out:
        return out["result"]
    else:
        return "Error."

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

