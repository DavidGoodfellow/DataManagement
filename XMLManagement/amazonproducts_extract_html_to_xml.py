import sys
from lxml import etree
from io import StringIO

def part1():
    
    #open and convert into tree
    filename = sys.argv[1]
    page = open(filename)
    text = page.read().decode("utf8")
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(text), parser)
    
    #filter out the full elements
    entries = []
    entries = tree.xpath('//li[starts-with(@id, resource_)]/node()')
    
    #filter for title names
    #leave title blank if there is none
    titles = []
    titles = tree.xpath('//li[starts-with(@id, resource_)]//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]/text()')
    
    #iterate through titles and xpath attach through that
    #1. get attribute that has a child a with @title=name of title
    #2. from that attribute, li[@class=attribute]/
    das = []
    resources = tree.xpath('//li[starts-with(@id, resource_)]/@id')
    for resource in resources:
        da = tree.xpath('//li[@id="'+resource+'"]//div[@class="a-row a-spacing-none"]/span[@class="a-size-small a-color-secondary"]//text()')
        if(len(da) > 0):
            das.append(da)
    
    #filter by author/date & for repeats
    filter_out = ['TODAY, ', 'Tomorrow, ', 'Monday,', 'Tuesday,', 'Wednesday,', 
                  'Thursday,', 'Friday,', 'Saturday,', 'Sunday,', 'by ', 'Get it by ', 
                  'FREE Shipping on eligible orders', ' and ', 'More Buying Choices',
                  'Get it ', 'Ships when available in 1-2 days.']
    months = ['Jan ','Feb ','Mar ','Apr ','May ','Jun ','Jul ','Aug ','Sep ',
              'Oct ','Nov ','Dec ','20']
    
    #creating list of dictionaries for each book
    entries = []
    entry = {}
    entry["authors"] = []
    #author = []
    
    #fill dictionaries
    date_bool = False
    repeat = False
    count = 0
    for da in das:
        entry["title"] = titles[count]
        count += 1
        for x in da:
            for month in months:
                if x.startswith(month):
                    entry["publication_date"] = x
                    date_bool = True
            for o in filter_out:
                if x.startswith(o):
                    date_bool = True
            if not date_bool:
                for a in entry.get("authors",[]):
                    if x == a:
                        repeat = True
                if not repeat:
                    entry.setdefault("authors", []).append(x)
            repeat = False
            date_bool = False
        entries.append(entry)
        entry = {}   

    #convert to xml
    xml = ['<books>']
    for entry in entries:
        xml.append('\t<book>')
        #replacing error value '&' and removing '
        title_edit = entry["title"].replace("&", "and")
        xml.append('\t\t<title>{0}</title>'.format(title_edit))
        if "publication_date" in entry:
            xml.append('\t\t<publication_date>{0}</publication_date>'.format(entry["publication_date"]))
        if len(entry.get("authors",[])) > 0:
            for author in entry.get("authors",[]):
                author_edit = author.replace(" and ","")
                xml.append('\t\t<author>{0}</author>'.format(author_edit.encode('utf-8')))
        xml.append('\t</book>')
    xml.append('</books>')
    return '\n'.join(xml)       
    
if len(sys.argv) > 2:
    mydata = part1()
    #print mydata
    myfile = open(sys.argv[2], "w")  
    myfile.write(mydata) 
    
else:
    print("Error: Include a .html file (to convert) then a .xml file (to write to) to as arguments")