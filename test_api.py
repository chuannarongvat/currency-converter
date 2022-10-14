import unittest
from api import call_get


class TestAPI(unittest.TestCase):

    def test_api_get(self):
        self.test_url = "https://api.frankfurter.app/currencies"
        self.assertNotEqual(call_get(self.test_url), None)


if __name__ == '__main__':
    unittest.main()
