import datetime
import sys


def check_arguments(args):

    length_args = len(args)

    if length_args == 3:
        return True
    else:
        sys.exit("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")


def check_date(date):

    try:
        if date != datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        sys.exit("Provided date is invalid")
