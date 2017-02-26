import sys
import requests
import random
import json

def StringSeperator(myString):
    while len(myString) != 0:
        punctuation = min(x for x in (myString.find(". "), myString.find(".\n"), myString.find("!"), myString.find("?")) if x > 0) + 1
        #print (punctuation)
        s = requests.Session()
        payload = {'txt': myString[0:punctuation]}
        r = s.post('http://sentiment.vivekn.com/api/text/', data=payload)
        j = r.json()
        prob = j['result']['confidence']
        emotion = j['result']['sentiment']
        if emotion != "Negative" and float(prob) >= 60.0:
            print(myString[0:punctuation]),
        else:
            x = random.randint(0,4)
            niceWords = ['I like puppies.', 'You look good today.', 'You\'re a smart and respected person.', 'I hope you have a wonderful day!', 'It\'s a good day to have a good day.']
            print (niceWords[x]),
        myString = myString[punctuation+1:len(myString)]
        # print (myString)

f = open(sys.argv[1], 'r')
StringSeperator(f.read())