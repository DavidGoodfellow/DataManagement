import sys
from pandas import read_csv

def part1():
    filename = sys.argv[1]
    readdata = read_csv(filename, delimiter = '\t')

    #map cols
    columns = []
    for col_name, col in readdata.transpose().iterrows():
        columns.append(col_name)
    
    #iterate through rows
    xml = ['<parks>']
    for row_name, row in readdata.iterrows():
        xml.append('\t<park>')
        i = 0
        for col in row:
            #remove the variables with no value
            if str(col) != 'nan':
                #replacing error value '&'
                col_edit = str(col).replace("&", "and")
                xml.append('\t\t<{0}>{1}</{0}>'.format(columns[i], col_edit))
            i = i + 1
        xml.append('\t</park>')    
    xml.append('</parks>')
    return '\n'.join(xml)


#runs if input is valid
if len(sys.argv) > 2:
    mydata = part1()
    myfile = open(sys.argv[2], "w")  
    myfile.write(mydata)  
    
else:
    print("Error: Include a .tsv file (to convert) then a .xml file (to write to) to as arguments")
    