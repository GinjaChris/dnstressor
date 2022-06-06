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
			tld = ["asia", "as", "au", "auto", "bid", "biz", "cn", "co", "com", "cz", "data", "de", "edu", "es", "expert", "flight", "game", "gov", "health", "homes", "hu", "int", "jp", "kp", "kr", "kv", "kz", "ru", "me", "media", "mil", "mo", "net", "ng", "nu", "online", "physics", "pl", "pk", "pr", "rs", "salon", "samsung", "silk", "sg", "tf", "ts", "ug", "uk", "us", "vip", "vu", "ws", "xyz", "yt", "zm", "zw"]
			tldout = random.choice(tld)
			nameout = randomstring + "." + tldout
			print(nameout)
			try:
					socket.gethostbyname(nameout)
			except:
					continue

threads = []

for i in range (40):
        t = threading.Thread(target=makedns)
        t.daemon = True
        threads.append(t)

for i in range (40):
        threads[i].start()

for i in range (40):
        threads[i].join()
