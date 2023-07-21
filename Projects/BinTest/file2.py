import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from binance.client import Client
import time

file = open("key.txt", "r")
lines = [line.rstrip("\n") for line in file]

key = lines[0].split(":")[1]
sec = lines[1].split(":")[1]
url = 'https://api.binance.com'
api_ep = '/api/v3/ticker/price'
headers = {
    'content-type': 'application/json',
    'X-MBX-APIKEY': key
}

s = requests.session()
s.headers.update(headers)

while True:
    response = s.get(url+api_ep, params={"symbol": "XRPBUSD"})
    print(response.json()['price'])
    time.sleep(1)


#
# client = Client(api_key=key, api_secret=sec, tld='us')
# syminfo = client.get_symbol_ticker(symbol='XRPBUSD')
# print(syminfo)