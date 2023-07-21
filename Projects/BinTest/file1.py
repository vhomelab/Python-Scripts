from binance.spot import Spot
import time

file = open("key.txt", "r")
lines = [line.rstrip("\n") for line in file]
# print((file.readline()).split(":")[1])
key = lines[0].split(":")[1]
# print(key)
sec = lines[1].split(":")[1]
# print(sec)
client = Spot()
print(client.time())
print(int(time.time()*1000) - client.time()['serverTime'])

client = Spot(api_key=key, api_secret=sec)
snap = client.account_snapshot()
print(snap)

