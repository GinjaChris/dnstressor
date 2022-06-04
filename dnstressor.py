import string
import random
import socket
import threading

def makedns():
	while True:
			randlen = random.randint(1,32)
			characters = "abcdefghijklmnopqrstuvwxyz0123456789-"
			length = 0
			randomstring = ""
			while length < randlen:
					randomstring += random.choice(characters)
					length = length + 1
			tld = ["com", "net", "xyz", "uk", "co", "cz", "kr", "au", "online", "cn", "hu", "health", "biz", "asia", "as", "auto", "mil", "edu", "int", "data", "bid", "es", "expert", "flight", "game", "gov", "homes", "kp", "kz", "kv",  "ru", "me", "media", "mo", "ng", "nu", "physics", "pl", "pk", "pr", "rs", "salon", "samsung", "silk", "sg", "tf", "ts", "us", "ug", "vip", "vu", "ws", "yt", "zm", "zw"]
			tldout = random.choice(tld)
			nameout = randomstring + "." + tldout
			print(nameout)
			try:
					socket.gethostbyname(nameout)
			except:
					continue

threads = []

for i in range (20):
        t = threading.Thread(target=makedns)
        t.daemon = True
        threads.append(t)

for i in range (20):
        threads[i].start()

for i in range (20):
        threads[i].join()
