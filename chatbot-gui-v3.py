# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dokumente/Python/chatbot_new/ressources/chatbot-gui-v3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from chatbot import Chatbot


class Ui_MainWindow(object):

    def Button_Los_click(self):
        zufallsantworten = ["Entschuldigung,das habe ich nicht verstanden!",
                        "Interessant",
                        "Ach wirklich...",
                        "Ich verstehe!"]
        reaktionen = {"hallo": "Schönen guten Tag!",
                  "geht": "Mir geht es gut! Und wie geht es Ihnen?",
                  "gefühle": "Das weiß ich nicht,denn ich habe keine Gefühle!"}

        if self.chatbot_input.text() == "":
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setText('Keine Eingabe!')
            message.setInformativeText('Ohne Frage kann ich nicht antworten!')
            message.exec_()
        else:
            bot = Chatbot(reaktionen, zufallsantworten)
            bot.set_Message(self.chatbot_input.text())
            self.label_Question.setText(bot.get_Response())
            self.chatbot_input.setText("")

    def Button_Bye_click(self):
        MainWindow.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 347)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 1061, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Welcome = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Welcome.setFont(font)
        self.label_Welcome.setObjectName("label_Welcome")
        self.verticalLayout.addWidget(self.label_Welcome)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label_Question = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setItalic(False)
        self.label_Question.setFont(font)
        self.label_Question.setObjectName("label_Question")
        self.verticalLayout.addWidget(self.label_Question)
        self.chatbot_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.chatbot_input.setFont(font)
        self.chatbot_input.setInputMask("")
        self.chatbot_input.setText("")
        self.chatbot_input.setObjectName("chatbot_input")
        self.verticalLayout.addWidget(self.chatbot_input)
        self.Button_Los = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Los.setGeometry(QtCore.QRect(870, 280, 100, 27))
        self.Button_Los.setObjectName("Button_Los")
        self.Button_Bye = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Bye.setGeometry(QtCore.QRect(980, 280, 100, 27))
        self.Button_Bye.setObjectName("Button_Bye")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.chatbot_input.returnPressed.connect(self.Button_Los_click)
        self.Button_Los.pressed.connect(self.Button_Los_click)
        self.Button_Bye.pressed.connect(self.Button_Bye_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chatbot-v3"))
        self.label_Welcome.setText(_translate("MainWindow", "Willkommen"))
        self.label_Question.setText(_translate("MainWindow", "Sprich mit mir..."))
        self.chatbot_input.setPlaceholderText(_translate("MainWindow", "an dieser Stelle..."))
        self.Button_Los.setText(_translate("MainWindow", "Go!"))
        self.Button_Bye.setText(_translate("MainWindow", "Bye"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
