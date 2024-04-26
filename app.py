import threading
from worker import walletbrute, walletbrute2
from util import configcls, CONFIGSTR, gen_mnemonic

def stop_app_thread(brute_thread, donecb):
	for i in range(0, len(brute_thread)):
		brute_thread[i]["s"]()

	for i in range(0, len(brute_thread)):
		brute_thread[i]["t"].join()
		print(f"Thread#{i} stopped")
	
	donecb()
	

def stop_app(brute_thread, donecb):
	sat = threading.Thread(target = stop_app_thread, args=(brute_thread, donecb))
	sat.start()
	print("Sending stop request")


def start_app(logcb, foundcb, coinlist, w3provider = None):
	brute_thread = {}
	configs = configcls()
	if len(coinlist) < 1:
		logcb("You need to enable at least one coin. Stop")
		return None
	max_thread = int(configs.get(CONFIGSTR.MAX_THREAD.value, 10))
	for i in range(0, max_thread):
		thread_ = walletbrute(w3provider, gen_mnemonic, coinlist)
		thread_.found_log_signal.connect(foundcb)
		thread_.run_log_signal.connect(logcb)
		thread_.set_func(configs.get(CONFIGSTR.MODULE.value, "demo"))
		tattr = {"t" : None, "s" : thread_.stop, "n" : ""}
		tattr["t"] = threading.Thread(target=thread_.run)
		brute_thread[i] = tattr
		brute_thread[i]["t"].start()
	logcb("Started")
	return brute_thread


def start_app_console(logcb, foundcb, coinlist, cfile, w3provider = None):
	brute_thread = {}
	configs = configcls(cfile)
	if len(coinlist) < 1:
		logcb("You need to enable at least one coin. Stop")
		return None
	max_thread = int(configs.get(CONFIGSTR.MAX_THREAD.value, 10))
	for i in range(0, max_thread):
		thread_ = walletbrute2(w3provider, gen_mnemonic, coinlist, logcb, foundcb)
		thread_.set_func(configs.get(CONFIGSTR.MODULE.value, "demo"))
		tattr = {"t" : None, "s" : thread_.stop, "n" : ""}
		tattr["t"] = threading.Thread(target=thread_.run)
		brute_thread[i] = tattr
		brute_thread[i]["t"].start()
	logcb("Started")
	return brute_thread