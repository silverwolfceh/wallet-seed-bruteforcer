from ui import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QCommandLinkButton,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)
import sys
from util import *

class uiaction(Ui_MainWindow):
    def __init__(self, MainWindow) -> None:
        super().__init__()
        self.setupUi(MainWindow)
        self.cfg = configcls()
        self.setupAction()

    def setupAction(self):
        for i in range(1, 7):
            checkbox = getattr(self, f"coin_{i}_cks")
            checkbox.clicked.connect(lambda state, name=checkbox: self.coin_x_change(state, name))
        
        

    def coin_x_change(self, event, sender):
        for i in range(1, 7):
            checkbox = getattr(self, f"coin_{i}_cks")
            if checkbox == sender:
                print(f"Check box {i}", sender.isChecked())
    



def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = uiaction(MainWindow)
    # ui.setupUi(MainWindow)
    # ui.setupAction()
    MainWindow.show()
    sys.exit(app.exec_())