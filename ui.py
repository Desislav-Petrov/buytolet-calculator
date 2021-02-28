# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(941, 522)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 410, 911, 51))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.calc_button = QPushButton(self.verticalLayoutWidget_3)
        self.calc_button.setObjectName(u"calc_button")

        self.verticalLayout_3.addWidget(self.calc_button)

        self.horizontalLayoutWidget_6 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(20, 310, 907, 41))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget_6)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10, 0, Qt.AlignLeft)

        self.weekly_profit_net = QLineEdit(self.horizontalLayoutWidget_6)
        self.weekly_profit_net.setObjectName(u"weekly_profit_net")
        self.weekly_profit_net.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.weekly_profit_net, 0, Qt.AlignHCenter)

        self.monthly_profit_net = QLineEdit(self.horizontalLayoutWidget_6)
        self.monthly_profit_net.setObjectName(u"monthly_profit_net")
        self.monthly_profit_net.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.monthly_profit_net, 0, Qt.AlignHCenter)

        self.yearly_profit_net = QLineEdit(self.horizontalLayoutWidget_6)
        self.yearly_profit_net.setObjectName(u"yearly_profit_net")
        self.yearly_profit_net.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.yearly_profit_net, 0, Qt.AlignHCenter)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 160, 911, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 230, 907, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5, 0, Qt.AlignLeft)

        self.weekly_management = QLineEdit(self.horizontalLayoutWidget_2)
        self.weekly_management.setObjectName(u"weekly_management")
        self.weekly_management.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.weekly_management, 0, Qt.AlignHCenter)

        self.monthly_management = QLineEdit(self.horizontalLayoutWidget_2)
        self.monthly_management.setObjectName(u"monthly_management")
        self.monthly_management.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.monthly_management, 0, Qt.AlignHCenter)

        self.yearly_management = QLineEdit(self.horizontalLayoutWidget_2)
        self.yearly_management.setObjectName(u"yearly_management")
        self.yearly_management.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.yearly_management, 0, Qt.AlignHCenter)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 190, 907, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.weekly_mortgage = QLineEdit(self.horizontalLayoutWidget_3)
        self.weekly_mortgage.setObjectName(u"weekly_mortgage")
        self.weekly_mortgage.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.weekly_mortgage, 0, Qt.AlignHCenter)

        self.monthly_mortgage = QLineEdit(self.horizontalLayoutWidget_3)
        self.monthly_mortgage.setObjectName(u"monthly_mortgage")
        self.monthly_mortgage.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.monthly_mortgage, 0, Qt.AlignHCenter)

        self.yearly_mortgage = QLineEdit(self.horizontalLayoutWidget_3)
        self.yearly_mortgage.setObjectName(u"yearly_mortgage")
        self.yearly_mortgage.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.yearly_mortgage, 0, Qt.AlignHCenter)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(20, 270, 907, 41))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.horizontalLayoutWidget_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.weekly_rent = QLineEdit(self.horizontalLayoutWidget_4)
        self.weekly_rent.setObjectName(u"weekly_rent")
        self.weekly_rent.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.weekly_rent, 0, Qt.AlignHCenter)

        self.monthly_rent = QLineEdit(self.horizontalLayoutWidget_4)
        self.monthly_rent.setObjectName(u"monthly_rent")
        self.monthly_rent.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.monthly_rent, 0, Qt.AlignHCenter)

        self.yearly_rent = QLineEdit(self.horizontalLayoutWidget_4)
        self.yearly_rent.setObjectName(u"yearly_rent")
        self.yearly_rent.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.yearly_rent, 0, Qt.AlignHCenter)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(20, 100, 911, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.horizontalLayoutWidget_5)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)

        self.tax_rate = QLineEdit(self.horizontalLayoutWidget_5)
        self.tax_rate.setObjectName(u"tax_rate")
        self.tax_rate.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.tax_rate, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_12 = QLabel(self.horizontalLayoutWidget_5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.management_fee_percent = QLineEdit(self.horizontalLayoutWidget_5)
        self.management_fee_percent.setObjectName(u"management_fee_percent")
        self.management_fee_percent.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.management_fee_percent, 0, Qt.AlignLeft)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_13 = QLabel(self.horizontalLayoutWidget_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_4.addWidget(self.label_13, 0, Qt.AlignLeft)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.tax_free_amount = QLineEdit(self.horizontalLayoutWidget_5)
        self.tax_free_amount.setObjectName(u"tax_free_amount")
        self.tax_free_amount.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.tax_free_amount, 0, Qt.AlignLeft)

        self.horizontalLayoutWidget_7 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(20, 30, 921, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_7)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7, 0, Qt.AlignLeft)

        self.property_price = QLineEdit(self.horizontalLayoutWidget_7)
        self.property_price.setObjectName(u"property_price")

        self.horizontalLayout_5.addWidget(self.property_price, 0, Qt.AlignLeft)

        self.label_8 = QLabel(self.horizontalLayoutWidget_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.rent_per_month = QLineEdit(self.horizontalLayoutWidget_7)
        self.rent_per_month.setObjectName(u"rent_per_month")

        self.horizontalLayout_5.addWidget(self.rent_per_month, 0, Qt.AlignLeft)

        self.label_9 = QLabel(self.horizontalLayoutWidget_7)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.loan_to_value_ratio = QLineEdit(self.horizontalLayoutWidget_7)
        self.loan_to_value_ratio.setObjectName(u"loan_to_value_ratio")

        self.horizontalLayout_5.addWidget(self.loan_to_value_ratio, 0, Qt.AlignLeft)

        self.label_15 = QLabel(self.horizontalLayoutWidget_7)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_5.addWidget(self.label_15)

        self.mortgage_ir = QLineEdit(self.horizontalLayoutWidget_7)
        self.mortgage_ir.setObjectName(u"mortgage_ir")

        self.horizontalLayout_5.addWidget(self.mortgage_ir, 0, Qt.AlignLeft)

        self.horizontalLayoutWidget_8 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(20, 350, 907, 41))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.horizontalLayoutWidget_8)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_10.addWidget(self.label_16, 0, Qt.AlignLeft)

        self.weekly_yield = QLineEdit(self.horizontalLayoutWidget_8)
        self.weekly_yield.setObjectName(u"weekly_yield")
        self.weekly_yield.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.weekly_yield, 0, Qt.AlignHCenter)

        self.monthly_yield = QLineEdit(self.horizontalLayoutWidget_8)
        self.monthly_yield.setObjectName(u"monthly_yield")
        self.monthly_yield.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.monthly_yield, 0, Qt.AlignHCenter)

        self.yearly_yield = QLineEdit(self.horizontalLayoutWidget_8)
        self.yearly_yield.setObjectName(u"yearly_yield")
        self.yearly_yield.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.yearly_yield, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 941, 30))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.calc_button.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Profit net", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Category/Period", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Weekly", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Monthly", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Yearly", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Management", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Mortgage", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Rent", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Tax Rate", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Management fee %", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Tax free p/a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Property Price", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rent p/m", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Loan to Value", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Mortage IR", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Yield %", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

