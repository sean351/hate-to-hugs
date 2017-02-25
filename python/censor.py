import sys
import requests
import random
import json
s = requests.Session()

for arg in sys.argv:
    if ".py" not in arg:
    
        payload = {'txt' : arg}
        r = s.post('http://sentiment.vivekn.com/api/text/', data=payload)
       # print(payload) #here for debugging

        j = r.json()
        # print (type(j))
        prob = j['result']['confidence']
        emotion = j['result']['sentiment']
        # print (prob)

        if emotion != "Negative" and float(prob) >= 50.0:
            print(arg)
        else:
            x = random.randint(0,2)
            niceWords = ['I like puppies.', 'You look good today.', 'You\'re a smart and respected person.']
            print (niceWords[x])
    
