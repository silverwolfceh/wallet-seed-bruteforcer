import threading
import importlib.util
import importlib.machinery


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
        try:
            spec = importlib.util.spec_from_file_location(mname, f"coinspecific/{mname}")
            loader = importlib.machinery.SourcelessFileLoader(mname, f"coinspecific/{mname}")
            module = importlib.util.module_from_spec(spec)
            loader.exec_module(module)
            self.func = getattr(module, 'checkBalance')
        except FileNotFoundError:
            print(f"Module {mname} not found.")
        except AttributeError:
            print(f"Function checkBalance not found in module {mname}.")

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
