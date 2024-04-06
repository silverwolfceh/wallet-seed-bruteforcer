import traceback

def getWallet(w3, my_mnemonic):
	w3.eth.account.enable_unaudited_hdwallet_features()
	account = w3.eth.account.from_mnemonic(my_mnemonic, account_path="m/44'/60'/0'/0/0")
	#account_BTC = w3.eth.account.from_mnemonic(my_mnemonic, account_path="m/44'/0'/0'/0/0")
	return account

def checkBalance(w3, words):
	account = getWallet(w3, words)
	#https://api-eu1.tatum.io/v3/bitcoin/address/balance/
	try:
		eth=w3.eth.get_balance(account.address)
		return eth
	except Exception as e:
		traceback.print_exc()
		return 0