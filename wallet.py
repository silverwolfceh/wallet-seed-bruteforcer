import traceback

accountpath = {
	"BTC" : "m/44'/0'/0'/0/0",
	"ETH" : "m/44'/60'/0'/0/0",
	"BNB" : "m/44'/714'/0'/0/0"
}

def get_balance(w3, my_mnemonic, cointype):
	w3.eth.account.enable_unaudited_hdwallet_features()
	account = w3.eth.account.from_mnemonic(my_mnemonic, account_path=accountpath[cointype])
	try:
		eth=w3.eth.get_balance(account.address)
		return eth
	except Exception as e:
		traceback.print_exc()
		return 0

def checkBalance(w3, words, coinlist):
	if coinlist == None:
		coinlist = accountpath

	for k,v in coinlist.items():
		bl = get_balance(w3, words, k)
		if bl > 0:
			return True, k, bl
	return False, "", 0 