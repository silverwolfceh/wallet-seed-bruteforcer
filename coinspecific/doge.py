import requests
from cryptofuzz import Dogecoin, Convertor,Ethereum

def checkBalance(w3, words, c):
    return checkCoinBalance(words, c)


def checkCoinBalance(words, coin):
    obj_mapping = {
        "DOGE" : Dogecoin,
        "ETH" : Ethereum,
    }
    api_to_check = {
        "DOGE" : "https://dogecoin.atomicwallet.io/api/v2/address/",
        "ETH" : "https://ethbook.guarda.co/api/v2/address/",
        "BNB" : "https://bsc-nn.atomicwallet.io/api/v2/address/"
    }
    if coin in obj_mapping:
        currencycls = obj_mapping[coin]()
        conv = Convertor()
        convert_hex = conv.mne_to_hex(words)
        currencyaddr = currencycls.hex_addr(convert_hex)
        for nw, url in api_to_check.items():
            try:
                url = url + currencyaddr
                req = requests.get(url)
                if req.status_code == 200:
                    bal = req.json()["balance"]
                    bal = int(bal)
                    if bal > 0:
                        return True, nw, bal
                    else:
                        continue
            except Exception as e:
               pass
        return False, coin, 0

def initModule():
    # Check license

    return True

def makingCake(cakeid):
    pass

def listCoin():
    return ["DOGE", "ETH"]