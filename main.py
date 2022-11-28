import requests
from requests.auth import AuthBase
import json, hmac, hashlib, time, base64

ACCESS_KEY = "L3drKMRZ1BFYHp8U"
API_SECRET = "1Ikj9rdRSeGTEE5J3y3OPsDYV4PKUYmh"

def get_all_accounts():
    timestamp = str(int(time.time())) 
    method="GET"
    url_path="/api/v3/brokerage/accounts"
    body=""
    message = timestamp + method + url_path + body;
    #hmac_key = base64.b64decode(API_SECRET);
    #signature = hmac.new(hmac_key, message.encode('utf-8'), digestmod=hashlib.sha256)
    #signature_b64 = base64.b64encode(signature.digest());
    signature = hmac.new(API_SECRET.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()
    print(signature.hex())
    url = "https://coinbase.com/api/v3/brokerage/accounts"
    headers = {
        "accept": "application/json",
        "CB-ACCESS-KEY": ACCESS_KEY,
        "CB-ACCESS-SIGN": signature.hex(),
        "CB-ACCESS-TIMESTAMP": timestamp
    }

    response = requests.get(url, headers=headers)
    print(response)
    print(response.text)

def get_account_detail(uuid):
    timestamp = str(int(time.time())) 
    method="GET"
    url_path="/api/v3/brokerage/accounts/"+uuid
    body=""
    message = timestamp + method + url_path + body;
    signature = hmac.new(API_SECRET.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()
    url = "https://coinbase.com/api/v3/brokerage/accounts/"+uuid
    headers = {
        "accept": "application/json",
        "CB-ACCESS-KEY": ACCESS_KEY,
        "CB-ACCESS-SIGN": signature,
        "CB-ACCESS-TIMESTAMP": timestamp
    }

    response = requests.get(url, headers=headers)
    print(response.text)

def create_order(client_order_id, product_id, side, order_configuration):
    timestamp = str(int(time.time())) 
    method="POST"
    url_path="/api/v3/brokerage/orders"
    body={
        "client_order_id": client_order_id,
        "product_id": product_id,
        "side": side,
        "order_configuration": order_configuration
    }
    message = timestamp + method + url_path + json.dumps(body);
    signature = hmac.new(API_SECRET.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()
    url = "https://coinbase.com/api/v3/brokerage/orders"
    headers = {
        "accept": "application/json",
        "CB-ACCESS-KEY": ACCESS_KEY,
        "CB-ACCESS-SIGN": signature,
        "CB-ACCESS-TIMESTAMP": timestamp,
        "content-type": "application/json"
    }

    response = requests.post(url, json=body, headers=headers)
    print(response.text)

def get_all_products():
    timestamp = str(int(time.time())) 
    method="GET"
    url_path="/api/v3/brokerage/products"
    body=""
    message = timestamp + method + url_path + body;
    #hmac_key = base64.b64decode(API_SECRET);
    #signature = hmac.new(hmac_key, message.encode('utf-8'), digestmod=hashlib.sha256)
    #signature_b64 = base64.b64encode(signature.digest());
    signature = hmac.new(API_SECRET.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()
    print(signature.hex())
    url = "https://coinbase.com/api/v3/brokerage/products"
    headers = {
        "accept": "application/json",
        "CB-ACCESS-KEY": ACCESS_KEY,
        "CB-ACCESS-SIGN": signature.hex(),
        "CB-ACCESS-TIMESTAMP": timestamp
    }

    response = requests.get(url, headers=headers)
    print(response)
    print(response.text)

get_all_products()