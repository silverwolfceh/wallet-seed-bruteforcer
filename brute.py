import threading
import time
from wallet import checkBalance
from mnemonic import Mnemonic

class walletbrute(threading.Thread):
    def __init__(self, callback, w3, genfunc, coinlist, logcb = print):
        threading.Thread.__init__(self)
        self.foundcb = callback
        self.w3 = w3
        self.gen = genfunc
        self.coinlist = coinlist
        self.logcb = logcb
        self.running = True
    
    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            w = self.gen()
            try:
                r, coin, bl = checkBalance(self.w3, w, self.coinlist)
                if r:
                    self.foundcb(w, coin, bl)
                self.logcb(f"Balance: {bl} - {w} \n")
            except Exception as e:
                print(w)
                print(e)

