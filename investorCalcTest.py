import investorCalc
import unittest


class TestInvestorCalc(unittest.TestCase):

    def test_per_month_to_period_week(self):
        self.assertEqual(investorCalc.per_month_to_period(100, 'WEEK'), 25)

    def test_per_month_to_period_month(self):
        self.assertEqual(investorCalc.per_month_to_period(100, 'MONTH'), 100)

    def test_per_month_to_period_year(self):
        self.assertEqual(investorCalc.per_month_to_period(100, 'YEAR'), 1200)

    def test_per_month_to_period_unknown(self):
        self.assertEqual(investorCalc.per_month_to_period(100, 'SOME'), None)


if __name__ == '__main__':
    unittest.main()
