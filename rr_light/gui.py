# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui-interface_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 460)
        MainWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);font-size:15pt;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);font-size:15pt;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet("font-size:14pt; color:rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("font-size:14pt; color:rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setStyleSheet("font-size:14pt; color:rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);font-size:15pt;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
<<<<<<< HEAD
        spacerItem = QtWidgets.QSpacerItem(
            5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem, 0, 1, 3, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet(
            "background-color: rgb(167, 169, 167);font-size:10pt;"
        )
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
=======
        spacerItem = QtWidgets.QSpacerItem(5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 3, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("background-color: rgb(167, 169, 167);font-size:10pt;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
>>>>>>> ff48205a005a9faf69479ceed45e9730549ea0bb
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("color:rgb(255, 255, 255);font-size:12pt;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("color:rgb(255, 255, 255);font-size:12pt;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("color:rgb(255, 255, 255);font-size:12pt;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
<<<<<<< HEAD
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
=======
        spacerItem3 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
>>>>>>> ff48205a005a9faf69479ceed45e9730549ea0bb
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(225, 225, 225); font-size:25px;")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)
<<<<<<< HEAD
        spacerItem4 = QtWidgets.QSpacerItem(
            448, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_4.addItem(spacerItem4, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            1, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout_4.addItem(spacerItem5, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
=======
        spacerItem4 = QtWidgets.QSpacerItem(448, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(1, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
>>>>>>> ff48205a005a9faf69479ceed45e9730549ea0bb
        self.gridLayout_5.addItem(spacerItem6, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reflection And Refraction"))
<<<<<<< HEAD
        self.label_4.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:16pt;">n</span><span style=" font-size:16pt; vertical-align:sub;">2</span><span style=" font-size:16pt;"> = </span></p></body></html>',
            )
        )
        self.label_2.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:16pt;">???</span><span style=" font-family:\'Symbol\'; font-size:16pt;">a</span><span style="font-size:16pt;"> =</span></p></body></html>',
            )
        )
        self.label_3.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:16pt;">n</span><span style=" font-size:16pt; vertical-align:sub;">1</span><span style=" font-size:16pt;"> =</span></p></body></html>',
            )
        )
        self.pushButton.setText(_translate("MainWindow", "Calculate And Show Graph"))
        self.label_5.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:16pt;">???</span><span style=" font-family:\'Symbol\'; font-size:16pt;">a =</span></p></body></html>',
            )
        )
        self.label_6.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-size:16pt;\">???</span><span style=\" font-family:'Symbol'; font-size:16pt;\">a</span><span style=\" font-family:'Nimbus Roman No9 L','Times New Roman','Times','serif'; font-size:16pt;\">???</span><span style=\" font-family:'Symbol'; font-size:16pt;\"> =</span></p></body></html>",
            )
        )
        self.label_7.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:16pt;">???</span><span style=" font-family:\'Symbol\'; font-size:16pt;">b =</span></p></body></html>',
            )
        )
        self.label.setWhatsThis(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.label.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600;">Reflection and Refraction of Light</span></p></body></html>',
            )
        )
=======
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">n</span><span style=\" font-size:16pt; vertical-align:sub;\">2</span><span style=\" font-size:16pt;\"> = </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">???</span><span style=\" font-family:\'Symbol\'; font-size:16pt;\">a</span><span style=\"font-size:16pt;\"> =</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">n</span><span style=\" font-size:16pt; vertical-align:sub;\">1</span><span style=\" font-size:16pt;\"> =</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Calculate And Show Graph"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">???</span><span style=\" font-family:\'Symbol\'; font-size:16pt;\">a =</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">???</span><span style=\" font-family:\'Symbol\'; font-size:16pt;\">a</span><span style=\" font-family:\'Nimbus Roman No9 L\',\'Times New Roman\',\'Times\',\'serif\'; font-size:16pt;\">???</span><span style=\" font-family:\'Symbol\'; font-size:16pt;\"> =</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">???</span><span style=\" font-family:\'Symbol\'; font-size:16pt;\">b =</span></p></body></html>"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Reflection and Refraction of Light</span></p></body></html>"))
>>>>>>> ff48205a005a9faf69479ceed45e9730549ea0bb
