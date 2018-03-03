import sys
from firebase import firebase
import re

#search if inputs given
def search():
    input = sys.argv[1]
    search = re.findall(r"[\w']+", str(input))
    fb = firebase.FirebaseApplication('https://shaped-buttress-160011.firebaseio.com', None)
    #search for ids
    ids = []
    x=0
    for item in search:
        result = fb.get('/Index/' + search[x].lower(), None)
        if result != None:
            for i in result:
                if i not in ids:
                    ids.append(i)
        x = x + 1

#runs if input is valid
if len(sys.argv) > 1:
    search()