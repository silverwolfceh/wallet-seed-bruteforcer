from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QTextCursor, QDesktopServices
from PySide6.QtCore import Slot, QUrl
from ui import Ui_MainWindow
import sys
from util import *
from app import start_app, stop_app
from web3.auto import Web3
import queue
from datetime import datetime

class uiaction(QMainWindow, Ui_MainWindow):
    def __init__(self, ver = "") -> None:
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.cfg = configcls()
        self.coinlist = []
        self.alchemy = None
        self.app_thread = []
        self.alive = True
        self.valid = True
        self.cur_state = APPLABLE.STOP
        self.next_state = APPLABLE.START
        self.log_q = queue.Queue()
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
        self.zalobtn.clicked.connect(lambda: self.open_contact(self.zalobtn))
        self.discordbtn.clicked.connect(lambda: self.open_contact(self.discordbtn))
        self.telegrambtn.clicked.connect(lambda: self.open_contact(self.telegrambtn))

    def export_hits(self):
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_path, _ = file_dialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            data = self.foundlog.toPlainText()
            with open(file_path, "w") as file:
                file.write(data)
            self.log_cb(f"Exported hit to {file_path}")

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
                if self.app_thread:
                    # Set the state
                    self.startstopbtn.setText(self.cur_state.value)
                    self.cur_state = APPLABLE.RUNNING
                    self.handle_state_update()
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

    def handle_ui_change(self, enable = False):
        self.modulenamecbx.setDisabled(enable)
        self.teleenablecks.setDisabled(enable)
        self.chantxt.setDisabled(enable)
        self.tokentxt.setDisabled(enable)
        self.maxthreadtxt.setDisabled(enable)
        for i in range(1, MAX_NUMBER_OF_COINS):
            checkbox = getattr(self, f"coin_{i}_cks")
            checkbox.setDisabled(enable)


    def handle_state_update(self):
        if self.cur_state == APPLABLE.RUNNING:
            self.handle_ui_change(True)
        else:
            self.handle_ui_change(False)
            

    def done_cb(self):
        self.log_cb("Stopped")
        self.cur_state = APPLABLE.STOP
        self.startstopbtn.setEnabled(True)
        self.startstopbtn.setText(APPLABLE.START.value)
        self.handle_state_update()

    @Slot(str)
    def log_cb(self, log):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.runningLog.append(f"[{formatted_time}] {log}")
        cursor = self.runningLog.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.runningLog.setTextCursor(cursor)
        self.runningLog.ensureCursorVisible()

    @Slot(str, str, float)
    def found_cb(self, w, coin, bl):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        data = f"[{formatted_time}] {coin} : {bl} -- Key/Menonic: {w}"
        self.foundlog.append(data)
        cursor = self.foundlog.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.foundlog.setTextCursor(cursor)
        self.foundlog.ensureCursorVisible()

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
            self.log_cb("Sorry, your module is not valid")
            self.startstopbtn.setDisabled(True)
        else:
            for i in range(1, len(coins) + 1):
                checkbox = getattr(self, f"coin_{i}_cks")
                checkbox.setText(coins[i-1])
                checkbox.show()
                checkbox.setChecked(False)

            for i in range(len(coins) + 1, MAX_NUMBER_OF_COINS):
                checkbox = getattr(self, f"coin_{i}_cks")
                checkbox.hide()
                checkbox.setChecked(False)
            self.startstopbtn.setDisabled(False)

    def module_name_change(self, mname):
        self.load_checkbox_coin(mname)
        self.cfg.set(CONFIGSTR.MODULE.value, mname)

    def coin_x_change(self, event, sender):
        for i in range(1, MAX_NUMBER_OF_COINS):
            checkbox = getattr(self, f"coin_{i}_cks")
            coinname = checkbox.text()
            if checkbox == sender:
                if sender.isChecked():
                    self.coinlist.append(coinname)
                    print(f"[{coinname}] is enable")
                else:
                    self.coinlist.remove(coinname)
                    print(f"[{coinname}] is disable")
    
    def open_contact(self, sender):
        url = ""
        if sender == self.zalobtn:
            url = "https://zalo.me/g/vtltxs287"
        elif sender == self.discordbtn:
            url = "https://discord.gg/PzJ7spKRdp"
        elif sender == self.telegrambtn:
            url = "https://t.me/seedBruteforcer"
        path = QUrl(url)
        QDesktopServices.openUrl(path)

    def closeEvent(self, event):
        print("Clean up")
        self.alive = False
        event.accept()




def start_gui(ver):
    app = QApplication(sys.argv)
    MainWindow = uiaction()
    # ui = uiaction(MainWindow)
    # ui.setupUi(MainWindow)
    # ui.setupAction()
    MainWindow.show()
    sys.exit(app.exec_())