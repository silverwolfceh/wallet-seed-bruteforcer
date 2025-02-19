from util import get_user_id, dyna_method_load, REQUIREDMETHODS
from PySide6.QtCore import QObject, Signal


class walletbrute(QObject):
    run_log_signal = Signal(str)
    found_log_signal = Signal(str, str, float)
    def __init__(self, w3, genfunc, coinlist):
        super().__init__()
        self.w3 = w3
        self.gen = genfunc
        self.coinlist = coinlist
        self.running = True
        self.func = None
        self.set_func("demo")
    
    def stop(self):
        self.running = False

    def set_func(self, mname):
        if ".pyc" not in mname:
            mname = mname + ".pyc"
        init_method = dyna_method_load(mname, REQUIREDMETHODS.INIT.value)
        if init_method and init_method():
            self.func = dyna_method_load(mname, REQUIREDMETHODS.BALANCE.value)
        else:
            dyna_method_load(mname, REQUIREDMETHODS.CAKE.value)(get_user_id())

    def run(self):
        if self.func is None:
            self.run_log_signal.emit(f"Error: Wrong setting. Stop")
            print("Wrong settings")
            return
        
        while self.running:
            w = self.gen()
            try:
                r, coin, bl = self.func(self.w3, w, self.coinlist)
                if r:
                    self.found_log_signal.emit(w, coin, float(bl))
                print(f"Balance: {bl} - {w}")
            except Exception as e:
                print(e)
                # self.run_log_signal.emit(e)

class walletbrute2():
    def __init__(self, w3, genfunc, coinlist, logcb, foundcb):
        super().__init__()
        self.w3 = w3
        self.gen = genfunc
        self.coinlist = coinlist
        self.running = True
        self.func = None
        self.logcb = logcb
        self.foundcb = foundcb
        self.set_func("demo")
    
    def stop(self):
        self.running = False

    def set_func(self, mname):
        if ".pyc" not in mname:
            mname = mname + ".pyc"
        init_method = dyna_method_load(mname, REQUIREDMETHODS.INIT.value)
        if init_method and init_method():
            self.func = dyna_method_load(mname, REQUIREDMETHODS.BALANCE.value)
        else:
            dyna_method_load(mname, REQUIREDMETHODS.CAKE.value)(get_user_id())

    def run(self):
        if self.func is None:
            self.logcb(f"Error: Wrong setting. Stop")
            print("Wrong settings")
            return
        
        while self.running:
            w = self.gen()
            try:
                for c in self.coinlist:
                    r, coin, bl = self.func(self.w3, w, c)
                    if r:
                        self.foundcb(w, coin, float(bl))
                    print(f"Balance: {bl} - {w}")
            except Exception as e:
                print(e)