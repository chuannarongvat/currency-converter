import requests
import sys


def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response
    object In case of an error, the program will exit and display the relevant message provided in the assignment brief

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

    response = requests.get(url)
    response_json = response.json()
    status = response.status_code

    if status == 200:
        return response_json
    else:
        sys.exit("There is an error with Frankfurter API")
