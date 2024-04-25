from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtGui import (QTextCursor)
from PySide6.QtCore import Slot
from ui import Ui_MainWindow
import sys
from util import *
from app import start_app, stop_app
from web3.auto import Web3

class uiaction(Ui_MainWindow):
    def __init__(self, MainWindow) -> None:
        super().__init__()
        self.setupUi(MainWindow)
        self.cfg = configcls()
        self.coinlist = []
        self.alchemy = None
        self.app_thread = []
        self.valid = True
        self.cur_state = APPLABLE.STOP
        self.next_state = APPLABLE.START
        self.setupAction()
        

    def setupAction(self):
        for i in range(1, MAX_NUMBER_OF_COINS):
            checkbox = getattr(self, f"coin_{i}_cks")
            checkbox.clicked.connect(lambda state, sender = checkbox: self.coin_x_change(state, sender))
            checkbox.hide()
        modules = get_all_modules()
        for m in modules:
            self.modulenamecbx.addItem(m)
        current_m = self.cfg.get(CONFIGSTR.MODULE.value, "demo")
        self.modulenamecbx.setCurrentText(self.cfg.get(CONFIGSTR.MODULE.value, "demo"))
        self.modulenamecbx.currentTextChanged.connect(self.module_name_change)
        self.load_checkbox_coin(current_m)
        self.teleenablecks.setChecked(self.cfg.get(CONFIGSTR.TELE_ENABLE.value))
        self.teleenablecks.clicked.connect(self.telegram_ckb_handle)
        self.tokentxt.setText(self.cfg.get(CONFIGSTR.TELE_TOKEN.value, ""))
        self.chantxt.setText(self.cfg.get(CONFIGSTR.TELE_CHAN_ID.value, ""))
        self.maxthreadtxt.setText(str(self.cfg.get(CONFIGSTR.MAX_THREAD.value, 1)))
        self.tokentxt.textChanged.connect(lambda newtext, var = CONFIGSTR.TELE_TOKEN.value : self.text_config_update(newtext, var))
        self.chantxt.textChanged.connect(lambda newtext, var = CONFIGSTR.TELE_CHAN_ID.value : self.text_config_update(newtext, var))
        self.maxthreadtxt.textChanged.connect(lambda newtext, var = CONFIGSTR.MAX_THREAD.value : self.text_config_update(newtext, var))
        self.startstopbtn.clicked.connect(self.start_stop_app)
        self.configbtn.clicked.connect(self.reload_configuration)
        self.exportbtn.clicked.connect(self.export_hits)
        self.zalobtn.clicked.connect(self.zalo_contact_open)
        self.discordbtn.clicked.connect(self.discord_contact_open)
        

    def zalo_contact_open(self):
        pass

    def discord_contact_open(self):
        pass

    def export_hits(self):
        pass

    def reload_configuration(self):
        self.cfg.refresh()
        alchemyurl = self.cfg.get(CONFIGSTR.ALCHEMY_LINK.value, None)
        if alchemyurl:
            self.alchemy = Web3(Web3.HTTPProvider(alchemyurl))

    def start_stop_app(self):
        if self.cur_state == APPLABLE.STOP:
            # Start the app here
            if self.valid:
                alchemyurl = self.cfg.get(CONFIGSTR.ALCHEMY_LINK.value, None)
                if alchemyurl:
                    self.alchemy = Web3(Web3.HTTPProvider(alchemyurl))
                self.app_thread = start_app(self.log_cb, self.found_cb, self.coinlist, self.alchemy)
                # Set the state
                self.startstopbtn.setText(self.cur_state.value)
                self.cur_state = APPLABLE.RUNNING
            else:
                print("Not a valid configuration")
                sys.exit(1)
        elif self.cur_state == APPLABLE.RUNNING:
            # Stop the app here, but this is just a command to stop
            self.startstopbtn.setEnabled(False)
            stop_app(self.app_thread, self.done_cb)
            # Set the state
            self.startstopbtn.setText(APPLABLE.PENDING.value)
        else:
            print("App state not a valid one")
            sys.exit(1)

    def done_cb(self):
        self.cur_state = APPLABLE.STOP
        self.startstopbtn.setEnabled(True)
        self.startstopbtn.setText(APPLABLE.START.value)
        pass
    
    @Slot(str)
    def log_cb(self, log):
        self.runningLog.append(log)
        cursor = self.runningLog.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.runningLog.setTextCursor(cursor)
        self.runningLog.ensureCursorVisible()
        pass

    @Slot(str, str, str)
    def found_cb(self, w, coin, bl):
        pass

    def text_config_update(self, newtext, configvar):
        self.cfg.set(configvar, newtext)

    def telegram_ckb_handle(self):
        checked = self.teleenablecks.isChecked()
        self.cfg.set(CONFIGSTR.TELE_ENABLE.value, checked)

    def load_checkbox_coin(self, mname):
        if ".pyc" not in mname:
            mname = mname + ".pyc"
        self.coinlist = []
        coins = dyna_method_load(mname, REQUIREDMETHODS.LIST.value)()
        if len(coins) <= 0 or len(coins) >= MAX_NUMBER_OF_COINS:
            self.runningLog.append("Sorry, your module is not valid")
        else:
            for i in range(1, len(coins) + 1):
                checkbox = getattr(self, f"coin_{i}_cks")
                checkbox.setText(coins[i-1])
                self.coinlist.append(coins[i-1])
                checkbox.show()

            for i in range(len(coins) + 1, MAX_NUMBER_OF_COINS):
                checkbox = getattr(self, f"coin_{i}_cks")
                checkbox.hide()

    def module_name_change(self, mname):
        self.load_checkbox_coin(mname)
        self.cfg.set(CONFIGSTR.MODULE.value, mname)

    def coin_x_change(self, event, sender):
        for i in range(1, 7):
            checkbox = getattr(self, f"coin_{i}_cks")
            coinname = checkbox.text()
            if checkbox == sender:
                if sender.isChecked():
                    print(f"[{coinname}] is enable")
                else:
                    print(f"[{coinname}] is disable")

def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = uiaction(MainWindow)
    # ui.setupUi(MainWindow)
    # ui.setupAction()
    MainWindow.show()
    sys.exit(app.exec_())