from gui import start_gui
from util import *
from app import start_app_console, stop_app
import sys
import argparse

TOOL_VERSION = "4.0.1"


def log_cb(msg):
    pass

def console_mode(argv):
    parser = argparse.ArgumentParser(description=f'Wallet Bruteforcer Console {TOOL_VERSION}' )
    parser.add_argument('-l', '--coinlist', type=str, help='Coin list by commas', required=True)
    parser.add_argument('-m', '--module', type=str, help='Module name')
    parser.add_argument('-t', '--thread', type=str, help='Max thread')
    parser.add_argument('-c', '--config', type=str, help='Config file', required=True)
    args = parser.parse_args(argv[1:])
    try:
        with open(args.config) as f:
            f.read()
        config = configcls(args.config)
        coins = args.coinlist.split(",")
        alchemy = config.get(CONFIGSTR.ALCHEMY_LINK.value, "")
        if args.thread:
            config.set(CONFIGSTR.MAX_THREAD.value, int(args.thread))
        if args.module:
            config.set(CONFIGSTR.MODULE.value, args.module)
        threads = start_app_console(log_cb, print, coins, args.config, alchemy)
    except Exception as e:
        print(e)

def launch(argv):
    if len(argv) > 1:
        console_mode(argv)
    else:
        start_gui(TOOL_VERSION)

if __name__ == "__main__":
    launch(sys.argv)