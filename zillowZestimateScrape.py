
import pandas as pd
import zillow


props = pd.read_csv('properties-32803.csv')
print(props.head())


import config

key = config.zpid

api = zillow.ValuationApi()

address = "3400 Pacific Ave., Marina Del Rey, CA"
postal_code = "90292"

#data = api.GetSearchResults(key, address, postal_code)

import pprint
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(data.get_dict())
#print(data.get_dict()["zestimate"])

address = str(props["address"][0])+", Orlando, FL"

#data = api.GetSearchResults(key, address, postal_code)
#print(data.get_dict()["zestimate"]['amount'])

zestimate= []
zestimateDiff = []

postal_code = "32803"
for i in range(0,len(props['address'])):
    try:
        address = str(props["address"][i])+", Orlando, FL"
        data = api.GetSearchResults(key, address, postal_code)
        zestimate.append(data.get_dict()["zestimate"]['amount'])
        zestimateDiff.append(data.get_dict()["zestimate"]['amount'] - (float(props['price'][i].strip('$').replace(',',''))))
    except:
        zestimate.append(0)
        zestimateDiff.append(0)
print(len(props['address']))

props['zestimate'] = zestimate
props['zestimateDiff'] = zestimateDiff

props.to_excel('Zillow Zestimate Data.xlsx')
