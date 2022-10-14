import sys
from currency import CurrencyConverter
from checks import check_arguments, check_date

if __name__ == "__main__":

    input_arg = sys.argv
    del input_arg[0]

    if check_arguments(sys.argv):
        from_currency = str(input_arg[1])
        to_currency = str(input_arg[2])
        date = str(input_arg[0])

        if check_date(date):
            currency_converter = CurrencyConverter(from_currency=from_currency,
                                                   to_currency=to_currency,
                                                   date=date
                                                   )
            if currency_converter.check_currencies():
                currency_converter.get_historical_rate()
