import json
import requests

ticker_url = 'https://api.coinmarketcap.com/v2/ticker?structure=array'

limit = 100
start = 1
sort = 'id'
convert = 'USD'

choice = input("Do you want to pass any custom parameters? (y/n): ")

if choice == "y":
    limit = input("What is the custom limit? :")
    start = input("What is the start number? :")
    sort = input("What do you want to sort by? : ")
    convert = input("What is your local currency? :")

ticker_url += '&limit=' + limit + '&sort=' + sort + '&start=' + start + '&convert' + convert
request = requests.get(ticker_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))
