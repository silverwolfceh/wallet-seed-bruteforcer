import threading
import time
from wallet import checkBalance
from mnemonic import Mnemonic

class walletbrute(threading.Thread):
    def __init__(self, callback, w3, genfunc):
        threading.Thread.__init__(self)
        self.foundcb = callback
        self.w3 = w3
        self.gen = genfunc

    def run(self):
        while True:
            w = self.gen()
            try:
                eth = checkBalance(self.w3, w)
                if eth > 0:
                    self.foundcb(w, eth)
                print(f"Balance: {eth} - {w}")
            except Exception as e:
                print(w)
                print(e)

