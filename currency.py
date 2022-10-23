import sys
from frankfurter import Frankfurter


class CurrencyConverter:

    def __init__(self, from_currency, to_currency, date):

        self.from_currency = from_currency
        self.to_currency = to_currency
        self.date = date
        self.frankfurter = Frankfurter()
        self.amount = None
        self.rate = None
        self.inverse_rate = None

    def check_currencies(self):

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

        self.rate = self.round_rate(self.frankfurter.get_historical_rate(self.from_currency,
                                                                         self.to_currency,
                                                                         self.date,
                                                                         amount=1)
                                    )

        self.inverse_rate = self.round_rate(1 / self.rate)
        return self.inverse_rate

    def round_rate(self, rate):

        round_rate = round(rate, 4)
        return round_rate

    def get_historical_rate(self):

        self.rate = self.round_rate(self.frankfurter.get_historical_rate(self.from_currency,
                                                                         self.to_currency,
                                                                         self.date,
                                                                         amount=1)
                                    )

        sys.exit(f"The conversion rate on {self.date} from {self.from_currency} to {self.to_currency} was {self.rate}. "
                 f"The inverse rate was {self.reverse_rate()}")
