import threading
import time
from wallet import checkBalance
from mnemonic import Mnemonic

class walletbrute(threading.Thread):
    def __init__(self, callback, w3, genfunc, coinlist):
        threading.Thread.__init__(self)
        self.foundcb = callback
        self.w3 = w3
        self.gen = genfunc
        self.coinlist = coinlist

    def run(self):
        while True:
            w = self.gen()
            try:
                r, coin, bl = checkBalance(self.w3, w, self.coinlist)
                if r:
                    self.foundcb(w, coin, bl)
                print(f"Balance: {bl} - {w}")
            except Exception as e:
                print(w)
                print(e)

