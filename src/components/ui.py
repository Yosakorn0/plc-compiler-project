# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inputLayout = QHBoxLayout()
        self.inputLayout.setObjectName(u"inputLayout")
        self.input_label = QLabel(self.centralwidget)
        self.input_label.setObjectName(u"input_label")

        self.inputLayout.addWidget(self.input_label)

        self.input_text = QLineEdit(self.centralwidget)
        self.input_text.setObjectName(u"input_text")

        self.inputLayout.addWidget(self.input_text)


        self.verticalLayout.addLayout(self.inputLayout)

        self.buttonLayout = QGridLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")

        self.buttonLayout.addWidget(self.button_1, 0, 0, 1, 1)

        self.button_2 = QPushButton(self.centralwidget)
        self.button_2.setObjectName(u"button_2")

        self.buttonLayout.addWidget(self.button_2, 0, 1, 1, 1)

        self.button_and = QPushButton(self.centralwidget)
        self.button_and.setObjectName(u"button_and")

        self.buttonLayout.addWidget(self.button_and, 0, 2, 1, 1)

        self.button_or = QPushButton(self.centralwidget)
        self.button_or.setObjectName(u"button_or")

        self.buttonLayout.addWidget(self.button_or, 0, 3, 1, 1)

        self.button_equal = QPushButton(self.centralwidget)
        self.button_equal.setObjectName(u"button_equal")

        self.buttonLayout.addWidget(self.button_equal, 1, 4, 1, 1)

        self.button_clear = QPushButton(self.centralwidget)
        self.button_clear.setObjectName(u"button_clear")

        self.buttonLayout.addWidget(self.button_clear, 1, 5, 1, 1)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.outputLayout = QHBoxLayout()
        self.outputLayout.setObjectName(u"outputLayout")
        self.output_label = QLabel(self.centralwidget)
        self.output_label.setObjectName(u"output_label")

        self.outputLayout.addWidget(self.output_label)

        self.output_lcd = QLCDNumber(self.centralwidget)
        self.output_lcd.setObjectName(u"output_lcd")
        self.output_lcd.setDigitCount(1)

        self.outputLayout.addWidget(self.output_lcd)


        self.verticalLayout.addLayout(self.outputLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Propositional Logic Evaluator", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"Input:", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"t", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"f", None))
        self.button_and.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.button_or.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.button_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.button_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
    # retranslateUi

