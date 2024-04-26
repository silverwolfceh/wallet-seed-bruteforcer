import requests
from cryptofuzz import Dogecoin, Convertor

def checkBalance(w3, words, coinlist):
    func_mapping = {
        "DOGE" : checkBalanceDoge
    }
    for c in coinlist:
        if c in func_mapping:
            return func_mapping[c](words)

def checkBalanceDoge(words):
    doge = Dogecoin()
    conv = Convertor()
    convert_hex = conv.mne_to_hex(words)
    doge_addr = doge.hex_addr(convert_hex)
    try:
        url = f"https://dogecoin.atomicwallet.io/api/v2/address/{doge_addr}"
        req = requests.get(url)
        if req.status_code == 200:
            bal = req.json()["balance"]
            bal = int(bal) / 100000000
            if bal > 0:
                return True, "DOGE", bal
            return False, "DOGE", 0
        else:
           return False, "DOGE", 0
    except Exception as e:
        print(e)
        return False, "DOGE", 0

def initModule():
    # Check license

    return True

def makingCake(cakeid):
    pass

def listCoin():
    return ["DOGE"]

if __name__ == '__main__':
    import sys
    sys.path.append("..")
    from util import gen_mnemonic
    w = gen_mnemonic()
    print(checkBalance(None, w, []))