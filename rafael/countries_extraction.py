import ijson

jsonfile = 'Resources/weekly_json/2007-06-18_factbook.json'

with open(jsonfile, 'rb') as f:
    country = ijson.items(f, 'countries')
    for x in country:
        print(x)