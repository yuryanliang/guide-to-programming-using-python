import json
import urllib.request

import requests

url = 'http://www.quandl.com/api/v1/datasets/FRED/GDP.json'

# method 1
response1 = urllib.request.urlopen(url)
text = response1.read().decode()
dict1 = json.loads(text)

# method 2
response2 = requests.get(url)
dict2 = response2.json()

print("1" if dict1 == dict2 else "2")
