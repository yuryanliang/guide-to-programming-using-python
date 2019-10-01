import json
import time
import urllib.request
price = 9999
while price > 55:
    page = urllib.request.urlopen('https://store.google.com/ca/config/pixel_3?hl=en-CA')
    text = page.read().decode('utf8')
    dict= json.loads(text)
    index = text.find("$59")
    price = int(text[index+1: index +3])
    print(price)
    time.sleep(2)
print('buy')

