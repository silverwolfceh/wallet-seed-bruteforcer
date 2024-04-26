import random
import time

def checkBalance(w3, words, coinlist):
    # time.sleep(1)
    for c in coinlist:
        arandom = random.randint(0, 99)
        found = arandom % 2
        if found:
            return True, c, random.randint(1, 5)
        else:
            return False, c, 0

def initModule():
    return True

def makingCake(cakeid):
    return True

def validateLicense(userid):
    return True

def listCoin():
    return ["BTC", "ETH", "BNB", "SOL", "DOGE", "ENA"]