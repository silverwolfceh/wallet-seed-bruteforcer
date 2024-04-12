import requests
import threading
import time
import json
from enum import Enum

def init_telegram(token, chatid):
	try:
		url=f"https://api.telegram.org/bot{token}/sendMessage"
		requests.get(url, params = {"chat_id": chatid,"text": "Telegram connect successfully"})
	except Exception as e:
		print(e)

def send_found(wq, token, chatid, w, coin, bl):
	wq.put(f"{w} | {coin} | {bl}")
	if token is not None and token != "":
		data= f"I found it : {w} | {coin} | {bl}"
		url=f"https://api.telegram.org/bot{token}/sendMessage"
		requests.get(url, params = {"chat_id": chatid,"text":data})

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