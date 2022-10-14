import unittest
from checks import check_arguments, check_date


class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """

    # => To be filled by student
    def test_exactly_three_args(self):
        expect = True
        test = check_arguments(("2022-01-01", "GBP", "AUD"))
        self.assertEqual(expect, test)

    def test_missing_args(self):
        with self.assertRaises(SystemExit):
            check_arguments(("2022-01-01", "AUD"))

    def test_more_than_three_args(self):
        with self.assertRaises(SystemExit):
            check_arguments(("2022-01-01", "AUD", "EUR", "GBP"))


class TestCheckDate(unittest.TestCase):
    """
    Class used for testing the check_date() function from checks.py
    """

    # => To be filled by student

    def test_valid_date(self):
        expect = True
        test = check_date("2020-01-01")
        self.assertEqual(expect, test)

    def test_invalid_month(self):
        with self.assertRaises(SystemExit):
            check_date("2020-13-01")

    def test_invalid_date(self):
        with self.assertRaises(SystemExit):
            check_date("2020-01-32")

    def test_invalid_format(self):
        with self.assertRaises(SystemExit):
            check_date("2020/01/01")


if __name__ == '__main__':
    unittest.main()
