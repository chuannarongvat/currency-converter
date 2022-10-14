# Building Currency Converter in Python

## Author
Name: Narongvat Chingpayakmon  
Student ID: 14229898


## Description

A Python programme I developed will convert currencies using information retrieved from the open source API: (https://www.frankfurter.app/)

The Frankfurter API monitors the ECB's(European Central Bank) published foreign exchange reference rates. Every working day at roughly 16:00 CET, the data is updated [1].

This programme calculates and shows the exchange rate between two currencies (from currency & to currency) at a particular date. It also computes and displays the inverse exchange rate between those two currencies. 

The script is run using the following command:
```{python}
python main.py <date> <currency1> <currency2>
```

The application is built to identify and report problems such as invalid input format arguments (missing arguments, too many arguments, etc.), invalid currency input, incorrect date format input, and errors if an API endpoint is called improperly. 

<Some of the challenges you faced>
It's quite challenging to begin and adjust to the logic of coding for someone who, like myself, has no prior expertise with Python coding. I first hesitated between using Pycharm and VScode as my IDE, but it turns out that Pycharm is simpler for me to get started with. Most often, I discovered while testing the code, that there was an error message I couldn't interpret and had to research it. At first, I have a lot of difficulty figuring out how to test the code, and I believe that this process' logic differs differently from the code I previously did.  

<Some of the features you hope to implement in the future>

In the future, I hope to add features that allow users to manually enter the precise amount of money they want their conversion to be in, and it would also be great if users could manually enter the precise time.


## How to Set up

First you need to install the requests package, and run the test file before running the program.

- ```test_api.py```
- ```test_check.py```
- ```test_currency.py```
- ```test_frankfurter.py```

If the test Ran pass on every test case, it is good to go.



<Which Python version you used>

```python
import sys
sys.version
```

When completing the task, I ran in ```Python 3.10```.

<Which packages and version you used>

In the assignment, I use requests package in api.py to request the call API endpoint with 
requests.get(url) and the version is 2.28.1. The DateTime packages is the one come with the base PyPi and used to call
and check the date format, the version is 4.5.

```python
import requests
import DateTime
```

and for the test case, I imported the Unit test.

```python
import unittest
```

## How to Run the Program

<Provide instructions and examples>

For running the program, going to the Terminal and type the following format.

```python
python main.py <date> <currency1> <currency2>
```

- ```date``` - is the date you want to know the currency
- ```currency1``` - is currency you want to convert from
- ```currency2``` - is currency you want to convert to

```python
"The conversion rate on 2021-07-16 from GBP to AUD was 1.8649. The inverse rate was 0.5362"
```

In case, there are an errors, both in the input arguments, wrong date format, and incorrect currency input.
The program with print out the messages and exit the program.

```python
python main.py 2022-01-01 GBP

"[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>"
```
e.g. wrong input argument messages will pop up.

```python
python main.py 2022/01/01 GBP AUD

"Provided date is invalid"
```
e.g. wrong date format messages will pop up.

```python
python main.py 2022-01-01 AAA bbb

"AAA and bbb are not valid currency codes"
```

e.g. incorrect currencies input.



## Project Structure
<List all folders and files of this project and provide quick description for each of them>  

There are 5 modules use to run the program, and
- ```api.py```
- ```checks.py```
- ```currency.py```
- ```frankfurter.py```
- ```main.py```

4 test module use to test each module
- ```test_api.py```
- ```test_check.py```
- ```test_currency.py```
- ```test_frankfurter.py```


### ```api.py```

#### ```def call_get(url: str) -> requests.models.Response:```

In the ```api.py```, a Function name ```call_get(url)``` is used to check the status of ```response_json(url)```. If the
status checked is ```== 200``` the function will ```return``` the response as requests module.

```python
import requests
import sys


def call_get(url: str) -> requests.models.Response:
    response = requests.get(url)
    response_json = response.json()
    status = response.status_code
    if status == 200:
        return response_json
```

Else it will exit the program and display the message.

```python
    else:
        sys.exit("There is an error with Frankfurter API")
```

### ```checks.py```

In ```check.py```, there are two function to check the requirement before running the code and import the module to access the
script from another Python module.

```python
import Sys
import datetime
```  

#### ```def check_arguments(args):```

Functions ```check_argument``` will check if the input argument are exactly 3, and will ```return True``` if it is in the case.

```python
def check_arguments(args):
    length_args = len(args)
    if length_args == 3:
        return True
```

Else if it's not in the cases(missing argument, or too many arguments), it will exit the program and print out the
message.

```python
    else:
        sys.exit("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")
```

#### ```def check_date(date):```

Functions ```check_date``` will check if the input date is valid(in a correct format) and will ```return True``` if it's in the
case [2].

```python
def check_date(date):
    try:
        if date != datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
```
Else if it's not in the case(invalid date), it will exit the program and print out the message.
```python
    except ValueError:
        sys.exit("Provided date is invalid")
```

### ```frankfurter.py```

In ```frankfurtaer.py``` ```call_get``` function has been import from ```api``` module to call the (url) API endpoint.

```python
from api import call_get
```

Class ```Frankfurter``` was created as an object instructor, and contains the current instances function of the class,
which are:
- ```base_url : str ```
  - Base url to call from Frankfurter API
- ```currencies_url: str ```
  - Frankfurter endpoint for extracting currencies list
- ```historical_url : str```
  - Frankfurter endpoint for extracting historical currencies conversion rates
- ```currencies : list```
  - an empty list that will store all the available currencies.

```python
class Frankfurter:
    def __init__(self):
        self.base_url = "https://api.frankfurter.app/"
        self.currencies_url = "https://api.frankfurter.app/currencies"
        self.historical_url = "https://api.frankfurter.app/%(date)s?from=%(from_currency)s"
        self.currencies = []
```

#### ```def get_currencies_list(self):```

Functions ```get_currencies_list``` will loop through the dictionaries from ```self.currencies_url``` and will use ```append()```
function to added into the empty list called ```self.currencies```.

```python
def get_currencies_list(self):
    for key in call_get(self.currencies_url):
        self.currencies.append(key)
    return self.currencies
```

```python
['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
```

#### ```def check_currency(self):```

Fucntions ```check_currency``` will check if the currency that users provided is in the list of currency or not. It will
```return True``` if in the case.

```python
def check_currency(self, currency):
    if currency in Frankfurter.get_currencies_list(self):
        return True
```
Else, if it's not in the case(currency isn't in the currencies list), it will ```return False```.

```python
    else:
        return False
```

#### ```def get_historical_rate(self, from_currency, to_currency, from_date, amount=1)```

Fucntions ```get_historical_rate``` will call the API endpoint from historical url with ```call_get``` function from ```api.py```
and return rates.
- ```histrorical_endpoint``` - will input from_date as "date", and from_currency as "from_currency"
- ```historical_response``` - will use call_get function from api.py module to call the historical url
- ```rates``` - will call an attribute from the list of dictionary that users input as "to_currency"

```python
def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
    historical_endpoint = self.historical_url % {"date": from_date, "from_currency": from_currency}
    historical_response = call_get(f"{historical_endpoint}")
    rates = historical_response["rates"][f"{to_currency}"]
    return rates
```

### ```currency.py```
In ```currency.py``` ```import sys``` and ```Frankfurter``` function has been import from ```frankfurter``` module. 

```python
import sys
from frankfurter import Frankfurter
```

Class ```CurrencyConverter``` was created as an object instructor, and contains the current instances function of the class,
which are:
- ```from_currency : str ```
  - from_currency is the currency user want to convert from.
- ```to_currency: str ```
  - to_currency is the currency user want to convert to.
- ```date : str```
  - date that users want to covert.
- ```frankfurter : ```
  - calling method in Frankfurter class.
- ```amount : float```
  - The amount to be converted, stored as None.
- ```rate : float```
  - The conversion rate from (from_currency - to_currency), stored as None.
- ```inverese_rate : float ```
  - The conversion rate from (to_currency - from_currency), stored as None.

```python
class CurrencyConverter:
    def __init__(self, from_currency, to_currency, date):

        self.from_currency = from_currency
        self.to_currency = to_currency
        self.date = date
        self.frankfurter = Frankfurter()
        self.amount = None
        self.rate = None
        self.inverse_rate = None
```

#### ```def check_currencies(self):```
Fucntions ```check_currencies``` will check if the currency that users provided is in the list of currency or not.
- ```check_from_currency``` - will store the self.from_currency from frankfurter.check_currency.
- ```check_to_currency``` - will store the self.to_currency from frankfurter.check_currency.

```python
def check_currencies(self):
    check_from_currency = self.frankfurter.check_currency(self.from_currency)
    check_to_currency = self.frankfurter.check_currency(self.to_currency)
```

It will ```reture True```, it the currency was stored in the class attribute, and will display the meassage if it's not in the
case and exit the program.

```python
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
```

#### ```def reverse_rate(self):```
Fucntions ```reverse_rate``` will calculate the inverse rate from the rate and return the value.

```python
def reverse_rate(self):
        

    self.rate = self.round_rate(self.frankfurter.get_historical_rate(self.from_currency,
                                                                         self.to_currency,
                                                                         self.date,
                                                                         amount=1)
                                )

    self.inverse_rate = self.round_rate(1 / self.rate)
    return self.inverse_rate
```

#### ```def round_rate(self):```
Fucntions ```round_rate``` will round the input rate to the 4 decimal places and return the value.

```python
 def round_rate(self, rate):
    round_rate = round(rate, 4)
    return round_rate
```

#### ```def get_historical_rate(self):```
Fucntions ```get_historical_rate``` will ```call get_historical_rate``` from ```Frankfurter``` module, that will require 4 input
- ```from_currency```
- ```to_currency```
- ```date```
- ```amount```

and will display the message and exit the system.

```python
def get_historical_rate(self):
        

    self.rate = self.round_rate(self.frankfurter.get_historical_rate(self.from_currency,
                                                                         self.to_currency,
                                                                         self.date,
                                                                         amount=1)
                                )

    sys.exit(f"The conversion rate on {self.date} from {self.from_currency} to {self.to_currency} was {self.rate}. "
                 f"The inverse rate was {self.reverse_rate()}")

```

### ```main.py```

```main.py``` is the main module that will use to call and control other module to run the program. In ```main.py``` ```sys```, 
```CurrencyCoverter``` class, ```check_arguments```, and ```check_date``` functions were imported.

```python
import sys
from currency import CurrencyConverter
from checks import check_arguments, check_date

```
First, extract the input arguments and name as ```input_arg``` and then delete the first argument 
(the name of Python script)

```python
if __name__ == "__main__":
    input_arg = sys.argv # Extract the input arguments
    del input_arg[0]     # Delete the first argument (the name of python script e.g. main.py)

```

Provided the ```sys.argv``` to check in the ```check_arguments``` function and If it passed, created a variable:
- ```from_currency = input_arg[1]```
- ```to_currency = input_arg[2]```
- ```date = input_arg[3]```

```python
    if check_arguments(sys.argv):
        from_currency = str(input_arg[1])
        to_currency = str(input_arg[2])
        date = str(input_arg[0])
```

Position are followed by the following command:

```{python}
python main.py <date> <currency1> <currency2>
```

Then the program will check the date format by function ```check_date()```, and in case if the provided date is valid,
```CurrencyConverter``` class will be called and assigned

- ```from_currency```
- ```to_currency```
- ```date```

to the function

```python
        if check_date(date):
            currency_converter = CurrencyConverter(from_currency=from_currency,
                                                   to_currency=to_currency,
                                                   date=date
                                                   )
```

After that will check the currencies in the ```CurrencyConverter``` class. If it's in the case will call the function
```get_historical_rate``` to print out the message.

```python
            if currency_converter.check_currencies():
                currency_converter.get_historical_rate()
```

```python
"The conversion rate on 2021-07-16 from GBP to AUD was 1.8649. The inverse rate was 0.5362"
```

### ```test_api.py```

This module will use to check the ```api.py``` that every is running perfectly fine.

```python
import unittest
from api import call_get
```

Class ```TestApi(unittest.TestCase):``` was created as an object instructor, and contains the function call
```test_api_get(self):``` to test the scenario.

```python
    def test_api_get(self):
        self.test_url = "https://api.frankfurter.app/currencies"
        self.assertNotEqual(call_get(self.test_url), None)

```
- ```test_url``` - is the url that are using to test

The return result of ```call_get(url)``` should return the requests model response, and using ```assertNotequal()``` to test the 
scenario.

```python
        self.assertNotEqual(call_get(self.test_url), None)
```

### ```test_checks.py```
This module will use to check the ```checks.py``` that every is running perfectly fine.

```python
import unittest
from checks import check_arguments, check_date
```

There are 2 classes.
- ``` class TestCheckArguments(unittest.TestCase):```
- ``` class TestCheckDate(unittest.TestCase):```

#### ```class TestCheckArguments(unittest.TestCase):```

There will be 3 functions(test case) with 7 tests store in this class.

```python
class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """

    # => To be filled by student
    def test_exactly_three_args(self):
        expect = True
        test = check_arguments(("2022-01-01", "GBP", "AUD"))
        self.assertEqual(expect, test)
```

In the ```test_exactly_three_args(self)```, the variable call ```expect``` will store the expected result(```True```) and create the 
variable call **test** to store the function from check_arguments(), and will using self.assertEqual() to compare if 
the expected and test are equal.

```python
    def test_missing_args(self):
        with self.assertRaises(SystemExit):
            check_arguments(("2022-01-01", "AUD"))

    def test_more_than_three_args(self):
        with self.assertRaises(SystemExit):
            check_arguments(("2022-01-01", "AUD", "EUR", "GBP"))
```

While on the ```test_missing_args(self)``` & ```test_more_than_three_args(self)``` will use 
```self.assertRaise(SystemExit):``` to test because the return result, the system shoule Exit the program.

#### ``` class TestCheckDate(unittest.TestCase):```

There are 4 function(test case)
- ```def test_valid_date(self):```
- ```def test_invalid_month(self):```
- ```def test_invalid_date(self):```
- ```def test_invalid_format(self):```

```python
class TestCheckDate(unittest.TestCase):

    def test_valid_date(self):
        expect = True
        test = check_date("2020-01-01")
        self.assertEqual(expect, test)
```
```python
    def test_invalid_month(self):
        with self.assertRaises(SystemExit):
            check_date("2020-13-01")

    def test_invalid_date(self):
        with self.assertRaises(SystemExit):
            check_date("2020-01-32")

    def test_invalid_format(self):
        with self.assertRaises(SystemExit):
            check_date("2020/01/01")
```

### ```test_currency.py```
This module will use to check the ```currency.py```.

There are 5 classes, with 11 tests case.
- ```class TestCurrencyConverterInstantiation(unittest.TestCase):```
- ```class TestCurrencyCheck(unittest.TestCase):```
- ```class TestReverseRate(unittest.TestCase):```
- ```class TestRoundRate(unittest.TestCase):```
- ```class TestHistoricalRate(unittest.TestCase):```


```python
import unittest
from currency import CurrencyConverter
```

```class TestCurrencyConverterInstantiation(unittest.TestCase):``` will test instantiate of the 
```CurrencyCoverter class```, ```from_currency```, ```to_currency```, and ```date``` 

In the function, the variable call ```expect``` will store the expected result(currency) and create the 
variable call ```test``` to store the function from ```CurrencyConverter```, and will using ```self.assertEqual()``` to 
compare if the expected and test are equal.

```python
class TestCurrencyConverterInstantiation(unittest.TestCase):

    def test_instantiation_from_currency(self):
        expect = "GBP"
        test = CurrencyConverter("GBP", "AUD", "2022-01-01")
        self.assertEqual(expect, test.from_currency)
```  
  

```class TestCurrencyCheck(unittest.TestCase):``` will test ```CurrencyConverter.check_currencies()``` from ```currency.py```

There are 4 function(test case).
- ```test_true_to_false(self):```
- ```test_false_to_true(self):```
- ```test_false_to_false(self):```
- ```test_true_to_true(self):```


```python
class TestCurrencyCheck(unittest.TestCase):
    def test_true_to_false(self):
        with self.assertRaises(SystemExit):
            CurrencyConverter("USD", "AAA", "2022-01-01").check_currencies()

    def test_false_to_true(self):
        with self.assertRaises(SystemExit):
            CurrencyConverter("BBB", "USD", "2022-01-01").check_currencies()

    def test_false_to_false(self):
        with self.assertRaises(SystemExit):
            CurrencyConverter("AAA", "bbb", "2022-01-01").check_currencies()

    def test_true_to_true(self):
        expect = True
        test = CurrencyConverter("GBP", "AUD", "2022-01-01").check_currencies()
        self.assertEqual(expect, test)
```

```class TestReverseRate(unittest.TestCase):``` will test ```CurrencyConverter.reverse_rate()``` from ```currency.py```

```python
class TestReverseRate(unittest.TestCase):

    def test_reverse_rate(self):
        expect = 0.5381
        test = CurrencyConverter("GBP", "AUD", "2022-01-01").reverse_rate()
        self.assertEqual(expect, test)
```

```class TestRoundrate(unittest.TestCase):``` will test ```CurrencyConverter.round_rate()``` from ```currency.py```

There are 2 function(test case).
- ```def test_round_rate_pass(self):```
- ```def test_round_rate_pass(self):```

```python
class TestRoundRate(unittest.TestCase):

    def test_round_rate_pass(self):
        expect = round(1 / 1.8583, 4)
        test = CurrencyConverter("GBP", "AUD", "2022-01-01").round_rate(0.53812624)
        self.assertEqual(expect, test)

    def test_round_rate_fail(self):
        expect = round(1 / 1.8583, 3)
        test = CurrencyConverter("GBP", "AUD", "2022-01-01").round_rate(0.53812624)
        self.assertNotEqual(expect, test)
```

```class TestHistoricalRate(unittest.TestCase):``` will test ```CurrencyConverter.get_historical_rate()``` from ```currency.py```

```python
class TestHistoricalRate(unittest.TestCase):

    def test_historical_rate(self):
        with self.assertRaises(SystemExit):
            CurrencyConverter("GBP", "AUD", "2020-01-01").get_historical_rate()

```

### ```test.frankfurter.py```
This module will use to check the ```frankfurter.py```.

There are 4 classes, with 9 tests case.
- ```class TestUrl(unittest.TestCase):```
- ```class TestCurrenciesList(unittest.TestCase):```
- ```class TestCheckCurrency(unittest.TestCase):```
- ```class TestHistoricalRate(unittest.TestCase):```

```python
import unittest
from frankfurter import Frankfurter
```

```class TestUrl(unittest.TestCase):``` will test the url arrtribute in the ```Frankfurter``` class.

```python
class TestUrl(unittest.TestCase):

    def setUp(self) -> None:
        self.frankfurter = Frankfurter()
        self.base_url = "https://api.frankfurter.app/"
        self.currencies_url = "https://api.frankfurter.app/currencies"
        self.historical_url = "https://api.frankfurter.app/%(date)s?from=%(from_currency)s"

    def test_base_url(self):
        expect = self.base_url
        test = self.frankfurter.base_url
        self.assertEqual(expect, test)

    def test_currencies_url(self):
        expect = self.currencies_url
        test = self.frankfurter.currencies_url
        self.assertEqual(expect, test)

    def test_historical_url(self):
        expect = self.historical_url
        test = self.frankfurter.historical_url
        self.assertEqual(expect, test)
```

```class TestCheckCurrency(unittest.TestCase):``` will test the ```Frankfurter.check_currency()```
from ```frankfurter.py```

```python
class TestCheckCurrency(unittest.TestCase):
  
    def setUp(self) -> None:
        self.frankfurter = Frankfurter()

    def test_is_true(self):
        expect = True
        test = self.frankfurter.check_currency("AUD")
        self.assertEqual(expect, test)

    def test_is_false(self):
        expect = False
        test = self.frankfurter.check_currency("AAA")
        self.assertEqual(expect, test)

```

```class TestHistoricalRate(unittest.TestCase):``` will test the ```Frankfurter.get_historical_rate()```
from ```frankfurter.py```

```python
class TestHistoricalRate(unittest.TestCase):

    def setUp(self) -> None:
        self.frankfurter = Frankfurter()

    def test_historical_rate_GBP_AUD(self):
        expect = 1.8583
        test = self.frankfurter.get_historical_rate("GBP", "AUD", "2022-01-01")
        self.assertEqual(expect, test)

    def test_historical_rate_AUD_GBP(self):
        expect = 0.53812
        test = self.frankfurter.get_historical_rate("AUD", "GBP", "2022-01-01")
        self.assertEqual(expect, test)

```

## Citations
<Mention authors and provide links code you source externally>


[1] Documentation. (n.d.). Retrieved September 9, 2022, from https://www.frankfurter.app/docs/  
[2] Jacinda. (2013, June 1). Answer to “How do I validate a date string format in python?” Stack Overflow. https://stackoverflow.com/a/16870682

