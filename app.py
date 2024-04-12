import signal
from mnemonic import Mnemonic
from web3.auto import Web3
import threading
from brute import walletbrute
from util import configcls, CONFIGSTR, COINSTR



def gen_mnemonic():
	mnemo = Mnemonic("english")
	return mnemo.generate(strength=128)

def stop_app_thread(brute_thread, donecb):
	for i in range(0, len(brute_thread)):
		brute_thread[i].stop()

	for i in range(0, len(brute_thread)):
		brute_thread[i].join()
		print(f"Thread#{i} stopped")
	
	donecb()
	

def stop_app(brute_thread, donecb):
	sat = threading.Thread(target=stop_app_thread, args=(brute_thread, donecb))
	sat.start()
	print("Sending stop request")

def start_app(logcb, foundcb):
	brute_thread = {}
	configs = configcls()
	# https://eth-mainnet.g.alchemy.com/v2/OatS-qWUFcNjgKNFTrq1m14A9h51mX2N
	# w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/OatS-qWUFcNjgKNFTrq1m14A9h51mX2N"))
	w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/cVoH6Tl8hMagXnCBYRb3cl7wxj7TXbCu"))
	scoins = configs.get(CONFIGSTR.SUPPORT_COIN.value, COINSTR.DEFAULT_COIN.value)
	print(scoins)
	for i in range(0, configs.get(CONFIGSTR.MAX_THREAD.value, 10)):
		brute_thread[i] = walletbrute(foundcb, w3, gen_mnemonic, scoins, logcb)
		brute_thread[i].set_func(configs.get(CONFIGSTR.MODULE.value, "eth"))
		brute_thread[i].start()
	return brute_thread


if __name__ == '__main__':
	start_app(print, print)
	try:
		# Wait for the termination signal (Ctrl+C)
		signal.signal(signal.SIGINT, signal.SIG_DFL)
		#signal.pause()
	except KeyboardInterrupt:
		exit(0)
		
