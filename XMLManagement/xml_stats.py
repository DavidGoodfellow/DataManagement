import sys
from lxml import etree

def parseTree():
    #upload & parse
    filename = sys.argv[1]
    page = open(filename)
    text = page.read().decode("utf8")
    root = etree.XML(text) 
    
    d = {}
    for element in root.iter():
        for a in element:
            if a.tag == 'LocationType':
                key = a.text
                if key in d:
                     d[key] += 1
                else:
                     d[key] = 1
    
    for key in sorted(d.iterkeys()):
        print(str(key) + '\t' + str(d[key]))  
        
#runs if input is valid
if len(sys.argv) > 1:
    parseTree()
    
else:
    print("Error: Include a .xml file as an argument")
