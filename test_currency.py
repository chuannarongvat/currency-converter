import unittest
from currency import CurrencyConverter


class TestCurrencyConverterInstantiation(unittest.TestCase):

    def test_instantiation_from_currency(self):
        expect = "GBP"
        test = CurrencyConverter("GBP", "AUD", "2022-01-01")
        self.assertEqual(expect, test.from_currency)

    def test_instantiation_to_currency(self):
        expect = "AUD"
        test = CurrencyConverter("GBP", "AUD", "2022-01-01")
        self.assertEqual(expect, test.to_currency)

    def test_instantiation_date(self):
        expect = "2022-01-01"
        test = CurrencyConverter("GBP", "AUD", "2022-01-01")
        self.assertEqual(expect, test.date)


class TestCurrencyCheck(unittest.TestCase):

    def test_true_to_false(self):
        with self.assertRaises(SystemExit):
            CurrencyConverter("USD", "AAA", "2022-01-01").check_currencies()

    def test_false_to_true(self):
        with self.assertRaises(SystemExit):
            CurrencyConverter("BBB", "USD", "2022-01-01").check_currencies()

    def test_false_to_false(self):
        with self.assertRaises(SystemExit):
            CurrencyConverter("AAA", "bbb", "2022-01-01").check_currencies()

    def test_true_to_true(self):
        expect = True
        test = CurrencyConverter("GBP", "AUD", "2022-01-01").check_currencies()
        self.assertEqual(expect, test)


class TestReverseRate(unittest.TestCase):

    def test_reverse_rate(self):
        expect = 0.5381
        test = CurrencyConverter("GBP", "AUD", "2022-01-01").reverse_rate()
        self.assertEqual(expect, test)


class TestRoundRate(unittest.TestCase):

    def test_round_rate_pass(self):
        expect = round(1 / 1.8583, 4)
        test = CurrencyConverter("GBP", "AUD", "2022-01-01").round_rate(0.53812624)
        self.assertEqual(expect, test)

    def test_round_rate_fail(self):
        expect = round(1 / 1.8583, 3)
        test = CurrencyConverter("GBP", "AUD", "2022-01-01").round_rate(0.53812624)
        self.assertNotEqual(expect, test)


class TestHistoricalRate(unittest.TestCase):

    def test_historical_rate(self):
        with self.assertRaises(SystemExit):
            CurrencyConverter("GBP", "AUD", "2020-01-01").get_historical_rate()


if __name__ == '__main__':
    unittest.main()
