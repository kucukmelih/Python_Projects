import requests
import sys


if len(sys.argv) == 1:
        exit("Missing command-line argument ")
elif len(sys.argv) == 2:
    if sys.argv[1] == type(int) or type(float):
        try:
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            data = response.json()
            bitcoin_price = data['bpi']['USD']['rate_float']

            amount = float(sys.argv[1])
            dollars = amount * bitcoin_price

            print(f"${dollars:,.4f}")

        except requests.RequestException:
            ...
    else: exit("Command-line argument is not a number ")

