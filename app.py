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
# Brute thread control
brute_thread = {}
# No edit
wq = queue.Queue()


def gen():
	mnemo = Mnemonic("english")
	return mnemo.generate(strength=128)

def load_config():
	global MAX_THREAD, TELE_BOT_TOKEN, TELE_CHAT_ID, SUPPORT_COIN
	with open("config.json") as f:
		config = json.loads(f.read())
		MAX_THREAD = int(config["MAX_THREAD"])
		TELE_BOT_TOKEN = config["TELE_TOKEN"]
		TELE_CHAT_ID = config["TELE_CHAN_ID"]
		SUPPORT_COIN = config["SUPPORT_COIN"]

def stop_app():
	pass


def start_app(maxthread, scancoin, logcb, foundcb):
	# https://eth-mainnet.g.alchemy.com/v2/OatS-qWUFcNjgKNFTrq1m14A9h51mX2N
	w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/cVoH6Tl8hMagXnCBYRb3cl7wxj7TXbCu"))
	load_config()
	# init_telegram()
	fthread = safefilewriter(wq)
	fthread.start()
	
	for i in range(0, maxthread):
		brute_thread[i] = walletbrute(foundcb, w3, gen, scancoin, logcb)
		brute_thread[i].start()
	return brute_thread


if __name__ == '__main__':
	start_app(print)
	
		
