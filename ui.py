# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledSxsMzF.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QCommandLinkButton,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(572, 626)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 561, 221))
        self.runningLog = QTextEdit(self.groupBox)
        self.runningLog.setObjectName(u"runningLog")
        self.runningLog.setGeometry(QRect(10, 20, 551, 201))
        self.runningLog.setLineWrapMode(QTextEdit.WidgetWidth)
        self.runningLog.setReadOnly(True)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 230, 561, 111))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 111, 16))
        self.label.setFont(font)
        self.modulenamecbx = QComboBox(self.groupBox_2)
        self.modulenamecbx.setObjectName(u"modulenamecbx")
        self.modulenamecbx.setGeometry(QRect(120, 20, 91, 22))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 71, 16))
        self.maxthreadtxt = QLineEdit(self.groupBox_2)
        self.maxthreadtxt.setObjectName(u"maxthreadtxt")
        self.maxthreadtxt.setGeometry(QRect(120, 50, 91, 21))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 81, 16))
        self.chantxt = QLineEdit(self.groupBox_2)
        self.chantxt.setObjectName(u"chantxt")
        self.chantxt.setGeometry(QRect(120, 80, 91, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.chantxt.setFont(font1)
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 80, 71, 20))
        self.tokentxt = QLineEdit(self.groupBox_2)
        self.tokentxt.setObjectName(u"tokentxt")
        self.tokentxt.setGeometry(QRect(290, 80, 181, 21))
        self.teleenablecks = QCheckBox(self.groupBox_2)
        self.teleenablecks.setObjectName(u"teleenablecks")
        self.teleenablecks.setGeometry(QRect(480, 80, 75, 20))
        self.coin_1_cks = QCheckBox(self.groupBox_2)
        self.coin_1_cks.setObjectName(u"coin_1_cks")
        self.coin_1_cks.setEnabled(True)
        self.coin_1_cks.setGeometry(QRect(230, 20, 91, 20))
        self.coin_4_cks = QCheckBox(self.groupBox_2)
        self.coin_4_cks.setObjectName(u"coin_4_cks")
        self.coin_4_cks.setGeometry(QRect(230, 50, 91, 20))
        self.coin_2_cks = QCheckBox(self.groupBox_2)
        self.coin_2_cks.setObjectName(u"coin_2_cks")
        self.coin_2_cks.setGeometry(QRect(330, 20, 91, 20))
        self.coin_3_cks = QCheckBox(self.groupBox_2)
        self.coin_3_cks.setObjectName(u"coin_3_cks")
        self.coin_3_cks.setGeometry(QRect(430, 20, 91, 20))
        self.coin_5_cks = QCheckBox(self.groupBox_2)
        self.coin_5_cks.setObjectName(u"coin_5_cks")
        self.coin_5_cks.setGeometry(QRect(330, 50, 91, 20))
        self.coin_6_cks = QCheckBox(self.groupBox_2)
        self.coin_6_cks.setObjectName(u"coin_6_cks")
        self.coin_6_cks.setGeometry(QRect(430, 50, 91, 20))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(1, 339, 561, 61))
        self.startstopbtn = QPushButton(self.groupBox_3)
        self.startstopbtn.setObjectName(u"startstopbtn")
        self.startstopbtn.setGeometry(QRect(110, 20, 101, 31))
        self.configbtn = QPushButton(self.groupBox_3)
        self.configbtn.setObjectName(u"configbtn")
        self.configbtn.setGeometry(QRect(220, 20, 101, 31))
        self.exportbtn = QPushButton(self.groupBox_3)
        self.exportbtn.setObjectName(u"exportbtn")
        self.exportbtn.setGeometry(QRect(330, 20, 101, 31))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 400, 561, 121))
        self.foundlog = QTextEdit(self.groupBox_4)
        self.foundlog.setObjectName(u"foundlog")
        self.foundlog.setGeometry(QRect(10, 20, 551, 101))
        self.foundlog.setLineWrapMode(QTextEdit.WidgetWidth)
        self.foundlog.setReadOnly(True)
        self.zalobtn = QCommandLinkButton(self.centralwidget)
        self.zalobtn.setObjectName(u"zalobtn")
        self.zalobtn.setGeometry(QRect(70, 530, 91, 41))
        icon1 = QIcon()
        icon1.addFile(u"../rokcontrol/rokcontrolweb/static/zalo.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.zalobtn.setIcon(icon1)
        self.discordbtn = QCommandLinkButton(self.centralwidget)
        self.discordbtn.setObjectName(u"discordbtn")
        self.discordbtn.setGeometry(QRect(190, 530, 101, 41))
        icon2 = QIcon()
        icon2.addFile(u"../rokcontrol/rokcontrolweb/static/discord.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.discordbtn.setIcon(icon2)
        self.discordbtn.setCheckable(False)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QRect(390, 520, 161, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wallet Scanner", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Scanning Log", None))
        self.runningLog.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Scanning log", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Choice module: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Thread #", None))
        self.maxthreadtxt.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Channel ID: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bot token:", None))
        self.teleenablecks.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.coin_1_cks.setText(QCoreApplication.translate("MainWindow", u"Dogecoin", None))
        self.coin_4_cks.setText(QCoreApplication.translate("MainWindow", u"Dogecoin", None))
        self.coin_2_cks.setText(QCoreApplication.translate("MainWindow", u"Dogecoin", None))
        self.coin_3_cks.setText(QCoreApplication.translate("MainWindow", u"Dogecoin", None))
        self.coin_5_cks.setText(QCoreApplication.translate("MainWindow", u"Dogecoin", None))
        self.coin_6_cks.setText(QCoreApplication.translate("MainWindow", u"Dogecoin", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.startstopbtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.configbtn.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.exportbtn.setText(QCoreApplication.translate("MainWindow", u"Export Hits", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Found log", None))
        self.foundlog.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Scanning log", None))
        self.zalobtn.setText(QCoreApplication.translate("MainWindow", u"Zalo", None))
        self.discordbtn.setText(QCoreApplication.translate("MainWindow", u"Discord", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Created by Eric The Cat", None))
    # retranslateUi

