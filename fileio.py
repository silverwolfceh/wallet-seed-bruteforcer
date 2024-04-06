import threading
import time

class safefilewriter(threading.Thread):
    def __init__(self, wq):
        threading.Thread.__init__(self)
        self.wq = wq

    def run(self):
        while True:
            data = self.wq.get()
            if data is None:
                self.fd.close()
                return
            with open("found.txt", "a+") as f:
                f.write(data + "\n")
            self.wq.task_done()
            time.sleep(2)
