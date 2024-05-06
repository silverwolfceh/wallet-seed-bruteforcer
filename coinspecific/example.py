import random
from typing import Tuple, List
import time

def checkBalance(w3, words, cointype) -> Tuple(bool, str, int):
    # Check the balance of the mnemonic: words with cointype: cointype
    # Return: True, cointype, balance if balance > 0
    # Return: False, cointype, 0 if balance <= 0
    return False, cointype, 0

def initModule() -> bool:
    # Any initialization should be call here
    return True

def makingCake(cakeid) -> bool:
    # A handle when the init is failed, you will get user fingerprint for blackist, ...
    return True

def validateLicense(userid) -> bool:
    # Function to validate if user is permit to use this module, self implementation
    # userid is passed from the main gui window with is an md5 of various finger print data
    return True

def listCoin() -> List:
    # A list of coin that support to check balance by this module.
    # Minimum of 1 and maximum of 6
    # Will be passed to the checkBalance function on last argument
    return ["BTC", "ETH", "BNB", "SOL", "DOGE", "ENA"]


'''
If you use additional library, please create a folder to collect the package (for example: newlib)
Then do the intallation of that additional library:
pip install package_name --target newlib
Then copy all the content in newlib and paste into the _internal folder (replaced if required)
'''