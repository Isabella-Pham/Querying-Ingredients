import urllib.request
import requests
import json
import operator

def get_api(query): #returns a dictionary of all the items in the api, if nothing shows up for query then returns statement saying to record manually
    query = query.replace(' ', '+')
    url = 'https://api.nal.usda.gov/ndb/search/?format=json&q=' + query + '&sort=n&offset=0&api_key=adBdNNK4tcs1RKpEOJnb6If4pZ9YH1B75ii9roZS&ds=Standard%20Reference'
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    if list(data.keys())[0] == 'errors':
        query = extractNouns(query)
        url = 'https://api.nal.usda.gov/ndb/search/?format=json&q=' + query + '&sort=n&offset=0&api_key=adBdNNK4tcs1RKpEOJnb6If4pZ9YH1B75ii9roZS&ds=Standard%20Reference'
        with urllib.request.urlopen(url) as url:
	        data = json.loads(url.read().decode())
        if list(data.keys())[0] == 'errors':
            return 'Must record information for "' + query + '" manually'
        else:
            return data['list']['item']
    return data['list']['item']

def getFrequencies(data): #determines the frequencies of each food group
    freqs = {'Dairy and Egg Products': 0, 'Spices and Herbs': 0, 'Baby Foods': 0, 'Fats and Oils': 0, 'Poultry Products': 0, 'Soups, Sauces, and Gravies': 0, 'Sausages and Luncheon Meats': 0,  'Breakfast Cereals': 0,  'Fruits and Fruit Juices': 0, 'Pork Products': 0, 'Vegetables and Vegetable Products': 0, 'Nut and Seed Products': 0, 'Beef Products': 0, 'Beverages': 0, 'Finfish and Shellfish Products': 0, 'Legumes and Legume Products': 0, 'Lamb, Veal, and Game Products': 0, 'Baked Products': 0, 'Sweets': 0, 'Cereal Grains and Pasta': 0, 'Fast Foods': 0, 'Meals, Entrees, and Side Dishes': 0, 'Snacks': 0, 'American Indian/Alaskan Native Foods': 0, 'Restaurant Foods': 0}
    for food in data:
        for info in food:
            if info == 'group':
                freqs = incrementFreq(freqs, food[info])
    return freqs

def incrementFreq(freqs, group): #takes in a food group and adds it to dictionary
    for key in freqs:
        if group==key:
            freqs[key] += 1
    return freqs

def getHighestFreq(freqs): #takes in dictionary of frequencies and returns most common group
	return max(freqs, key = freqs.get)

def getNDBNO(foodGroup, data): #returns the lowest NDBNO in the most prominent food group
    lowestNDBNO = {'Dairy and Egg Products': 0, 'Spices and Herbs': 0, 'Baby Foods': 0, 'Fats and Oils': 0, 'Poultry Products': 0, 'Soups, Sauces, and Gravies': 0, 'Sausages and Luncheon Meats': 0,  'Breakfast Cereals': 0,  'Fruits and Fruit Juices': 0, 'Pork Products': 0, 'Vegetables and Vegetable Products': 0, 'Nut and Seed Products': 0, 'Beef Products': 0, 'Beverages': 0, 'Finfish and Shellfish Products': 0, 'Legumes and Legume Products': 0, 'Lamb, Veal, and Game Products': 0, 'Baked Products': 0, 'Sweets': 0, 'Cereal Grains and Pasta': 0, 'Fast Foods': 0, 'Meals, Entrees, and Side Dishes': 0, 'Snacks': 0, 'American Indian/Alaskan Native Foods': 0, 'Restaurant Foods': 0} #dictionary of the lowest NDBNO numbers per food group
    group = ''
    for food in data:
        for info in food:
            if info == 'group':
                group = food[info]
            if info == 'ndbno':
                for key in lowestNDBNO:
                    if group == key and (int(food[info]) < lowestNDBNO[key] or lowestNDBNO[key] == 0):
                        lowestNDBNO[key] = int(food[info])
    NDBNO = lowestNDBNO[foodGroup]
    return NDBNO

def entropy(freqs): #determines whether or not the entropy is large enough
    highest = freqs[getHighestFreq(freqs)]
    for group in freqs:
        if abs(freqs[group] - highest) < 1 and group != getHighestFreq(freqs): #1 is just currently a placeholder
            return 'Entropy is too small, must deal with manually'
    return 'Entropy is large enough, do not have to deal with manually'

def extractNouns(query): #still in progress
    query = query.split()
	#for word in query:
		#INSERT TAGGING CODE HERE
    return query

#Below is code to test the functions written above
data = get_api('lasagna')
freqs = getFrequencies(data)
HighestFreq = getHighestFreq(freqs)
print(getNDBNO(HighestFreq, data))
