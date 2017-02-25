import sys
import requests

s = requests.Session()

for arg in sys.argv:
    if arg != "sentiment.py":
    
        payload = {'txt' : arg}
        r = s.post('http://sentiment.vivekn.com/api/text/', data=payload)
        print(payload)
        print(r.text)
    
