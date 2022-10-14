import unittest
from api import call_get


class TestAPI(unittest.TestCase):
    """
    Class used for testing the call_get() function in api.py
    """

    # => To be filled by student

    def test_api_get(self):
        self.test_url = "https://api.frankfurter.app/currencies"
        self.assertNotEqual(call_get(self.test_url), None)


if __name__ == '__main__':
    unittest.main()
