import requests
from cryptofuzz import Dogecoin, Convertor


def checkBalance(w3, words, coinlist):
    doge = Dogecoin()
    conv = Convertor()
    convert_hex = conv.mne_to_hex(words)
    doge_addr = doge.hex_addr(convert_hex)
    print("Doge address from words: ", doge_addr)
    try:
        url = f"https://dogecoin.atomicwallet.io/api/v2/address/{doge_addr}"
        req = requests.get(url)
        if req.status_code == 200:
            bal = req.json()["balance"]
            return int(bal) / 100000000
        else:
            return 0
    except Exception as e:
        print(e)
        return 0

def initModule():
    # Check license

    return True

def makingCake(cakeid):
    pass

def load_coins():
    return ["DOGE"]

if __name__ == '__main__':
    import sys
    sys.path.append("..")
    from util import gen_mnemonic
    w = gen_mnemonic()
    print(checkBalance(None, w, []))