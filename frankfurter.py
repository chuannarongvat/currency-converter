from api import call_get


class Frankfurter:

    def __init__(self):
        self.base_url = "https://api.frankfurter.app/"
        self.currencies_url = "https://api.frankfurter.app/currencies"
        self.historical_url = "https://api.frankfurter.app/%(date)s?from=%(from_currency)s"
        self.currencies = []

    def get_currencies_list(self):

        for key in call_get(self.currencies_url):
            self.currencies.append(key)
        return self.currencies

    def check_currency(self, currency):

        if currency in Frankfurter.get_currencies_list(self):
            return True
        else:
            return False

    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):

        historical_endpoint = self.historical_url % {"date": from_date, "from_currency": from_currency}
        historical_response = call_get(f"{historical_endpoint}")
        rates = historical_response["rates"][f"{to_currency}"]
        return rates
