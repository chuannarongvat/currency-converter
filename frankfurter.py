from api import call_get


class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will
    also automatically call the Currencies endpoint and store the return list of available currency codes.

    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint for extracting currencies list
    historical_url : str
        Frankfurter endpoint for extracting historical currencies conversion rates
    currencies: list
        List of available currency codes
    """

    def __init__(self):
        self.base_url = "https://api.frankfurter.app/"
        self.currencies_url = "https://api.frankfurter.app/currencies"
        self.historical_url = "https://api.frankfurter.app/%(date)s?from=%(from_currency)s"
        self.currencies = []

    def get_currencies_list(self):
        """
        Method that will get the list of available currencies and returns it as a Python list.

        Parameters
        ----------
        # => To be filled by student

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => To be filled by student
        """

        for key in call_get(self.currencies_url):
            self.currencies.append(key)
        return self.currencies

    def check_currency(self, currency):
        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise, it will return False.

        Parameters
        ----------
        # => To be filled by student

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => To be filled by student
        """

        if currency in Frankfurter.get_currencies_list(self):
            return True
        else:
            return False

    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and
        currencies. It will return a requests.models.Response object.

        Parameters
        ----------
        # => To be filled by student

        Pseudo-code
        ----------
        # => To be filled by student

        Returns
        -------
        # => To be filled by student
        """

        historical_endpoint = self.historical_url % {"date": from_date, "from_currency": from_currency}
        historical_response = call_get(f"{historical_endpoint}")
        rates = historical_response["rates"][f"{to_currency}"]
        return rates
