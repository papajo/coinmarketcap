import os
import json
import requests
from datetime imnport datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

convert = "USD"

listings_url = "https://api.coinmarketcap.com/v2/listings/?convert=" + convert

request = requests.get(listings_url)
results = request.json()
data = results['data']

ticker_url_pairs = {}
for currency in data:
    symbol = currency['symbol']
    url= currency['id']
    ticker_url_pairs[symbol] = url

    
