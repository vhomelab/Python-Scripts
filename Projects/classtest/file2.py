import os
import requests
import MyFunctions
import time

file = open("config.txt", "r")
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
    MyFunctions.clear()

