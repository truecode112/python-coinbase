import requests
import json, hmac, hashlib, time, base64

ACCESS_KEY = "L3drKMRZ1BFYHp8U"
API_SECRET = "1Ikj9rdRSeGTEE5J3y3OPsDYV4PKUYmh"

def get_all_accounts():
    timestamp = str(int(time.time())) 
    method="GET"
    url_path="/api/v3/brokerage/accounts"
    body=""
    message = timestamp + method + url_path + body;
    print(message)
    signature = hmac.new(API_SECRET.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()
    print(signature.hex(), timestamp)
    url = "http://coinbase.com/api/v3/brokerage/accounts"
    headers = {
        "accept": "application/json",
        "CB-ACCESS-KEY": ACCESS_KEY,
        "CB-ACCESS-SIGN": signature,
        "CB-ACCESS-TIMESTAMP": timestamp
    }

    response = requests.get(url, headers=headers)
    print(response.text)

def get_account_detail(uuid):
    timestamp = str(int(time.time())) 
    method="GET"
    url="/api/v3/brokerage/accounts"
    message = timestamp + method + url
    signature = hmac.new(API_SECRET.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()
    print(signature.hex(), timestamp)


get_all_accounts()