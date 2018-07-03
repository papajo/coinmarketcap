import json
import requests
#import urllib.request
global_url = "https://api.coinmarketcap.com/v2/global/"

request = requests.get(global_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))
#print(json.dumps(results.decode("utf-8"), sort_key=True, indent=4))
