# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageRetrieval(object):
    def setupUi(self, ImageRetrieval):
        ImageRetrieval.setObjectName("ImageRetrieval")
        ImageRetrieval.resize(880, 600)
        self.centralwidget = QtWidgets.QWidget(ImageRetrieval)
        self.centralwidget.setObjectName("centralwidget")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(750, 90, 91, 31))
        self.browseButton.setObjectName("browseButton")
        self.query_image = QtWidgets.QLabel(self.centralwidget)
        self.query_image.setGeometry(QtCore.QRect(750, 0, 81, 71))
        self.query_image.setObjectName("query_image")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 701, 551))
        self.widget.setObjectName("widget")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(750, 150, 91, 31))
        self.clearButton.setObjectName("clearButton")
        ImageRetrieval.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImageRetrieval)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 21))
        self.menubar.setObjectName("menubar")
        ImageRetrieval.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ImageRetrieval)
        self.statusbar.setObjectName("statusbar")
        ImageRetrieval.setStatusBar(self.statusbar)

        self.retranslateUi(ImageRetrieval)
        QtCore.QMetaObject.connectSlotsByName(ImageRetrieval)

    def retranslateUi(self, ImageRetrieval):
        _translate = QtCore.QCoreApplication.translate
        ImageRetrieval.setWindowTitle(_translate("ImageRetrieval", "MainWindow"))
        self.browseButton.setText(_translate("ImageRetrieval", "Browse Image"))
        self.query_image.setText(_translate("ImageRetrieval", "  Query Image"))
        self.clearButton.setText(_translate("ImageRetrieval", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageRetrieval = QtWidgets.QMainWindow()
    ui = Ui_ImageRetrieval()
    ui.setupUi(ImageRetrieval)
    ImageRetrieval.show()
    sys.exit(app.exec_())