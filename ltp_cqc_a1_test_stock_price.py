import ltp_cqc_a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_1(self):
        """Test stock_price_summary with empty list"""

        actual = ltp_cqc_a1.stock_price_summary([])
        expected = (0,0)
        self.assertEqual(actual,expected)

    def test_stock_price_summary_2(self):
        """Test stock_price_summary with a list of no gains and no losses"""

        actual = ltp_cqc_a1.stock_price_summary([0,0,0])
        expected = (0,0)
        self.assertEqual(actual,expected)

    def test_stock_price_summary_3(self):
        """Test stock_price_summary with only positive numbers"""

        actual = ltp_cqc_a1.stock_price_summary([0.1,0.03,0.04])
        expected = (0.17, 0)
        self.assertEqual(actual,expected)

    def test_stock_price_summary_4(self):
        """Test stock_price_summary with only negative numbers"""

        actual = ltp_cqc_a1.stock_price_summary([-0.1, -0.43,-0.001])
        expected = (0, -0.531)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_5(self):
        """Test stock_price_summary with both positive, negative numbers, and zero"""

        actual = ltp_cqc_a1.stock_price_summary([0.01, 0.05, -0.03, -0.4, 0, 0, 0.1, -0.33])
        expected = (0.16, -0.76)
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main(exit=False)
