import sys
import json
from pandas import read_csv
import pandas
import requests
import re

# =============================================================================
# Part 1
# =============================================================================

#read file
def part1():
    filename = sys.argv[1]
    readdata = read_csv(filename)
    #convert csv to json
    for index, row in readdata.iterrows():
        print row
        data.append(row)   
        df = pandas.DataFrame(data).to_json(orient='index')
    #send to firebase
    requests.put("https://shaped-buttress-160011.firebaseio.com/Recipes.json",df)
    #print requests.get("https://shaped-buttress-160011.firebaseio.com/Recipes.json")
# =============================================================================
# Part 2
# =============================================================================
#create reverse indexes
# =============================================================================
# def part2():
#     inverse_data = {}
#     x=0
#     while x < len(data):
#         temp = data[x]
#         array_to_add = re.findall(r"[\w']+", str(temp['event']))
#         for item in array_to_add:
#             if str(item).lower() in inverse_data:
#                 inverse_data[str(item).lower()].append(temp['id'])
#             else:
#                 inverse_data[str(item).lower()] = [temp['id']]
#         x = x + 1
#     #send results to firebase
#     json_inverse = json.dumps(inverse_data)
#     requests.put("https://shaped-buttress-160011.firebaseio.com/Index.json",json_inverse)
# =============================================================================

#runs if input is valid
if len(sys.argv) > 1:
    data = []
    part1()
    #part2()
