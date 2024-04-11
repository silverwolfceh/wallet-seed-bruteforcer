import traceback
from web3.auto import Web3


def get_balance(w3, my_mnemonic, cointype):
	# print(cointype)
	w3.eth.account.enable_unaudited_hdwallet_features()
	account = w3.eth.account.from_mnemonic(my_mnemonic, account_path=cointype)
	try:
		eth=w3.eth.get_balance(account.address)
		# print(eth)
		return eth
	except Exception as e:
		traceback.print_exc()
		return 0

def checkBalance(w3, words, coinlist):
	for k,v in coinlist.items():
		bl = get_balance(w3, words, v)
		if bl > 0:
			return True, k, bl
	return False, "", 0 

if __name__ == '__main__':
	w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/OatS-qWUFcNjgKNFTrq1m14A9h51mX2N"))
	word = "float bridge decline salmon visit mosquito smoke room giggle stamp normal unlock"
	coinlist = {'bnb' : "m/44'/60'/0'/0/0"}
	print(checkBalance(w3, word, coinlist))