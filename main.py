import sys
from currency import CurrencyConverter
from checks import check_arguments, check_date

if __name__ == "__main__":
    """
    Main logics of the program.

    Pseudo-code ---------- Extract the input arguments Remove the first argument (name of Python script) Check there 
    are 3 items in the remaining list of argument (using your defined check_arguments() function) Check the validity 
    of the input date (using your defined check_date() function) Instantiate an objet from your defined 
    CurrencyConverter class with the verified 2 currency codes and date Check the validity of the 2 currency codes (
    using your defined check_currencies() method from CurrencyConverter class) Extract the historical rate and 
    calculate its inverse rate (using your defined get_historical_rate() method from CurrencyConverter class) """

    # => To be filled by student

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
