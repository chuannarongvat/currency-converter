import unittest
from frankfurter import Frankfurter


class TestUrl(unittest.TestCase):
    """
    Class used for testing the url attributes of the Frankfurter class from checks.py
    """

    # => To be filled by student

    def setUp(self) -> None:
        self.frankfurter = Frankfurter()
        self.base_url = "https://api.frankfurter.app/"
        self.currencies_url = "https://api.frankfurter.app/currencies"
        self.historical_url = "https://api.frankfurter.app/%(date)s?from=%(from_currency)s"

    def test_base_url(self):
        expect = self.base_url
        test = self.frankfurter.base_url
        self.assertEqual(expect, test)

    def test_currencies_url(self):
        expect = self.currencies_url
        test = self.frankfurter.currencies_url
        self.assertEqual(expect, test)

    def test_historical_url(self):
        expect = self.historical_url
        test = self.frankfurter.historical_url
        self.assertEqual(expect, test)


class TestCurrenciesList(unittest.TestCase):
    """
    Class used for testing the currencies attribute of the Frankfurter class from checks.py
    """

    # => To be filled by student

    def setUp(self) -> None:
        frankfurter = Frankfurter()

        self.expected = [
            'AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS',
            'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'SEK', 'SGD', 'THB', 'TRY',
            'USD', 'ZAR']
        self.result = frankfurter.get_currencies_list()

    def test_count_eq(self):
        self.assertCountEqual(self.result, self.expected)

    def test_list_eq(self):
        self.assertListEqual(self.result, self.expected)


class TestCheckCurrency(unittest.TestCase):
    """
    Class used for testing the Frankfurter.check_currency() method from frankfurter.py
    """

    # => To be filled by student
    def setUp(self) -> None:
        self.frankfurter = Frankfurter()

    def test_is_true(self):
        expect = True
        test = self.frankfurter.check_currency("AUD")
        self.assertEqual(expect, test)

    def test_is_false(self):
        expect = False
        test = self.frankfurter.check_currency("AAA")
        self.assertEqual(expect, test)


class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the Frankfurter.get_historical_rate() method from frankfurter.py
    """

    # => To be filled by student

    def setUp(self) -> None:
        self.frankfurter = Frankfurter()

    def test_historical_rate_GBP_AUD(self):
        expect = 1.8583
        test = self.frankfurter.get_historical_rate("GBP", "AUD", "2022-01-01")
        self.assertEqual(expect, test)

    def test_historical_rate_AUD_GBP(self):
        expect = 0.53812
        test = self.frankfurter.get_historical_rate("AUD", "GBP", "2022-01-01")
        self.assertEqual(expect, test)


if __name__ == '__main__':
    unittest.main()
