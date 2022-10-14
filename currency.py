import sys
from frankfurter import Frankfurter


class CurrencyConverter:
    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes,
    date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    api : Frankfurter
        Instance of Frankfurter class
    """

    def __init__(self, from_currency, to_currency, date):
        # => To be filled by student

        self.from_currency = from_currency
        self.to_currency = to_currency
        self.date = date
        self.frankfurter = Frankfurter()
        self.amount = None
        self.rate = None
        self.inverse_rate = None

    def check_currencies(self):
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise, the program will exit and display the relevant message provided in the assignment brief

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

        # self.frankfurter.get_currencies_list()

        check_from_currency = self.frankfurter.check_currency(self.from_currency)
        check_to_currency = self.frankfurter.check_currency(self.to_currency)

        if not check_from_currency and not check_to_currency:
            print(f"{self.from_currency} and {self.to_currency} are not valid currency codes")
            sys.exit(0)

        elif check_from_currency:
            if check_to_currency:
                return True
            else:
                print(f"{self.to_currency} is not a valid currency code")
                sys.exit(0)
        else:
            print(f"{self.from_currency} is not a valid currency code")
            sys.exit(0)

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4
        decimal places and save it back in the class attribute inverse_rate.

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

        # => To be filled by student

        self.rate = self.round_rate(self.frankfurter.get_historical_rate(self.from_currency,
                                                                         self.to_currency,
                                                                         self.date,
                                                                         amount=1)
                                    )

        self.inverse_rate = self.round_rate(1 / self.rate)
        return self.inverse_rate

    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.

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

        round_rate = round(rate, 4)
        return round_rate

    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded
        to 4 decimals) and date stored in the class attributes. Then it will calculate the inverse rate and will exit
        by displaying the relevant message provided in the assignment brief

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

        self.rate = self.round_rate(self.frankfurter.get_historical_rate(self.from_currency,
                                                                         self.to_currency,
                                                                         self.date,
                                                                         amount=1)
                                    )

        sys.exit(f"The conversion rate on {self.date} from {self.from_currency} to {self.to_currency} was {self.rate}. "
                 f"The inverse rate was {self.reverse_rate()}")
