import datetime
import sys


def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input
    arguments if it is the case. Otherwise, the program will exit and display the relevant message provided in the
    assignment brief

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

    length_args = len(args)

    if length_args == 3:
        return True
    else:
        sys.exit("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")


def check_date(date):
    """
    Function that will check if the provided date is valid and will return the value True if that is the case.
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

    try:
        if date != datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        sys.exit("Provided date is invalid")
