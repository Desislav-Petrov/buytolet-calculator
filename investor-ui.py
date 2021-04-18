import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui import Ui_MainWindow

from investorCalc import *

class BuyToLetUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.management_fee_percent.setText(str(MANAGEMENT_FEE_PERCENT))
        self.tax_free_amount.setText(str(TAX_FREE_AMOUNT))

        # Slots/Signals
        self.calc_button.pressed.connect(self.calc)

    def calc(self):
        if not self.property_price.text():
            QMessageBox.warning(self, "Missing input!", "Please enter property price")
            return
        property_price = float(self.property_price.text())

        if not self.rent_per_month.text():
            QMessageBox.warning(self, "Missing input!", "Please enter rent per month")
            return
        rent_pm = float(self.rent_per_month.text())

        if not self.loan_to_value_ratio.text():
            QMessageBox.warning(self, "Missing input!", "Please enter LTV")
            return
        ltv = float(self.loan_to_value_ratio.text())

        if not self.mortgage_ir.text():
            QMessageBox.warning(self, "Missing input!", "Please enter mortgage interest rate")
            return
        mortgage_ir = float(self.mortgage_ir.text())

        if not self.mortgage_term.text():
            QMessageBox.warning(self, "Missing input!", "Please enter mortgage term in years")
            return
        mortgage_term = float(self.mortgage_term.text())

        # Mortgage
        self.weekly_mortgage.setText(str(calc_mortgage(property_price, ltv, mortgage_ir, mortgage_term, "WEEK")))
        self.monthly_mortgage.setText(str(calc_mortgage(property_price, ltv, mortgage_ir, mortgage_term, "MONTH")))
        self.yearly_mortgage.setText(str(calc_mortgage(property_price, ltv, mortgage_ir, mortgage_term, "YEAR")))

        # Management
        self.weekly_management.setText(str(calc_management_fee(rent_pm, "WEEK")))
        self.monthly_management.setText(str(calc_management_fee(rent_pm, "MONTH")))
        self.yearly_management.setText(str(calc_management_fee(rent_pm, "YEAR")))

        # Rent
        self.weekly_rent.setText(str(calc_rent(rent_pm, "WEEK")))
        self.monthly_rent.setText(str(calc_rent(rent_pm, "MONTH")))
        self.yearly_rent.setText(str(calc_rent(rent_pm, "YEAR")))

        # Profit net
        self.weekly_profit_net.setText(
            str(calc_profit_net(property_price, ltv, mortgage_ir, mortgage_term, rent_pm, "WEEK")))
        self.monthly_profit_net.setText(
            str(calc_profit_net(property_price, ltv, mortgage_ir, mortgage_term, rent_pm, "MONTH")))
        self.yearly_profit_net.setText(
            str(calc_profit_net(property_price, ltv, mortgage_ir, mortgage_term, rent_pm, "YEAR")))

        # Yield
        self.weekly_yield.setText(str(calc_yield(rent_pm, property_price, "WEEK")))
        self.monthly_yield.setText(str(calc_yield(rent_pm, property_price, "MONTH")))
        self.yearly_yield.setText(str(calc_yield(rent_pm, property_price, "YEAR")))

app = QApplication(sys.argv)
w = BuyToLetUI()
app.exec_()
