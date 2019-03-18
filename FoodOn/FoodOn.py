import urllib.request
import json
import operator
import nltk
import math

def get_FoodOn(query): #returns a dictionary of all the results for this query from FoodOn
    queryNoSpace = query.replace('_', '+')
    url = 'https://www.ebi.ac.uk/ols/api/search?q=' + queryNoSpace + '&groupField=iri&start=0&ontology=foodon'
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data['response']['docs']
    
def get_List(data):
    foods = []
    for items in data:
        foods.append(items['label'])
    return foods

data = get_FoodOn('parmigiano')
list = get_List(data)
print(list)
