import requests
import sys


def call_get(url: str) -> requests.models.Response:
    
    response = requests.get(url)
    response_json = response.json()
    status = response.status_code

    if status == 200:
        return response_json
    else:
        sys.exit("There is an error with Frankfurter API")
