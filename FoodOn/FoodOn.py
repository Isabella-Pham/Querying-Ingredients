import urllib.request
import json

def getFoodOn(query): #returns a dictionary of all the results for this query from FoodOn
    queryNoSpace = query.replace('_', '+')
    url = 'https://www.ebi.ac.uk/ols/api/search?q=' + queryNoSpace + '&groupField=iri&start=0&ontology=foodon'
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data['response']['docs']

def getID(data):
    foods = []
    for items in data:
        foods.append(items['short_form'])
    return foods[0]

def findParent(id): #given the foodOn ID of a query, determine its parent
    url = 'https://www.ebi.ac.uk/ols/api/ontologies/foodon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252F' + id + '/parents'
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data['_embedded']['terms'][0]['label']

def getParent(query):
    data = getFoodOn(query)
    id = getID(data)
    return findParent(id)

print(getParent('liquid_smoke'))
