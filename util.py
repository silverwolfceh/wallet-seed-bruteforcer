import requests
import threading
import time
import json
from enum import Enum
import py_compile
import os
import base64
import hashlib
import uuid

def make_modules():
	directory = "coinspecific"
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith(".py"):  # Check if the file is a Python file
				file_path = os.path.join(root, file)
				print(f"Compiling {file_path}...")
				try:
					py_compile.compile(file_path, cfile=os.path.join(root, file) + "c")
					print("Compilation successful!")
				except py_compile.PyCompileError as e:
					print(f"Compilation failed for {file_path}: {e}")

def init_telegram(token, chatid):
	try:
		url=f"https://api.telegram.org/bot{token}/sendMessage"
		requests.get(url, params = {"chat_id": chatid,"text": "Telegram connect successfully"})
	except Exception as e:
		print(e)

def send_found(wq, token, chatid, w, coin, bl):
	wq.put(f"{w} | {coin} | {bl}")
	try:
		if token is not None and token != "":
			data= f"I found it : {w} | {coin} | {bl}"
			url=f"https://api.telegram.org/bot{token}/sendMessage"
			requests.get(url, params = {"chat_id": chatid,"text":data})
	except Exception as e:
		print(e)

class safefilewriter(threading.Thread):
	def __init__(self, wq, fname = "found.txt"):
		threading.Thread.__init__(self)
		self.wq = wq
		self.fname = fname

	def run(self):
		while True:
			data = self.wq.get()
			if data is None:
				return
			with open(self.fname, "a+") as f:
				f.write(data + "\n")
			self.wq.task_done()
			time.sleep(2)
			

class configcls:
	def __init__(self):
		self.conf = None
		with open("config.json", "r") as f:
			self.conf = json.loads(f.read())
		
	def __save__(self):
		with open("config.json", "w") as f:
			f.write(json.dumps(self.conf, indent=4))

	def get(self, cname, dvalue = ""):
		if self.conf and cname in self.conf:
			return self.conf[cname]
		return dvalue
	
	def set(self, cname, cvalue):
		if self.conf:
			self.conf[cname] = cvalue
			self.__save__()
	
	def refresh(self):
		with open("config.json", "r") as f:
			self.conf = json.loads(f.read())
			


class CONFIGSTR(Enum):
	MAX_THREAD = "MAX_THREAD"
	SUPPORT_COIN = "SUPPORT_COIN"
	TELE_TOKEN = "TELE_TOKEN"
	TELE_CHAN_ID = "TELE_CHAN_ID"
	MODULE = "MODULE"
	LICENSE_KEY = "LICENSE"
	

class COINSTR(Enum):
	DEFAULT_COIN = {"ETH" : "m/44'/60'/0'/0/0"}
	BTC = "m/44'/0'/0'/0/0"
	ETH = "m/44'/60'/0'/0/0"
	BNB = "m/44'/714'/0'/0/0"
	SOL = "m/44'/501'/0'/0/0"

def coin_to_path(coinstr):
	cmap = {
		'btc' : COINSTR.BTC.value,
		'eth' : COINSTR.ETH.value,
		'bnb' : COINSTR.BNB.value,
		'sol' : COINSTR.SOL.value
	}

	for k,v in cmap.items():
		if coinstr.lower() == k:
			return v
	
	return None

def create_finger_print(username, mac_address, ipdata):
    data = username.encode() + mac_address.encode() + ipdata.encode()
    md5_hash = hashlib.md5(data).hexdigest()
    return md5_hash

def get_user_id():
	username = os.getlogin()
	mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
	res = requests.get('http://ip-api.com/json/')
	ipdata = json.dumps(res.json())
	return create_finger_print(username, mac_address, ipdata)

if __name__ == "__main__":
	make_modules()
	print(get_user_id())