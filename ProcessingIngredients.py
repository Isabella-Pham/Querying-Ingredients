from Querying import * #import file with functions to get NDBNO
import time
import matplotlib.pyplot as plot
import numpy as np

def getFood():
    with open ("list.txt", "r") as file:
        list = file.read().splitlines()
    return list

def percentage(processed, total): #returns the percentage of ingredients that do not need to be manually processed
    return (processed/total)*100 + '%'

def getFoodDescription(NDBNO): #NDBNO must be a String
    url = 'https://api.nal.usda.gov/ndb/reports/?ndbno=' + NDBNO + '&type=f&format=json&api_key=adBdNNK4tcs1RKpEOJnb6If4pZ9YH1B75ii9roZS'
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data['report']['food']['name']

def createHistogram(entropies):
    plot.hist(entropies,density=3,bins=10, facecolor='blue')
    plot.xlabel('Entropy')
    plot.ylabel('Frequency')
    plot.show()

def listNDBNO(list): #returns a dictionary of the food and it's NDBNO number
    total = 0;
    processed = 0;
    output = open('Output.txt', 'w')
    noResults = open('noResults.txt', 'w')
    highEntropy = open('HighEntropy.txt', 'w')
    entropies = []
    output.write('Below is a list of foods and their NDBNO numbers:' + '\n')
    noResults.write('Below is a list of foods that must be manually checked because they did not produce search results:' + '\n')
    highEntropy.write('Below is a list of foods that must be manually checked due to their high entropy:' + '\n')
    total = 0
    processed = 0
    for food in list:
        total = total + 1
        data = get_api(food)
        freqs = getFrequencies(data)
        print(food)
        if data == 'ERROR' or bool(freqs) == False:
            noResults.write(food + '\n')
            noResults.flush()
        elif getEntropy(freqs) > 2.1: #entropy cutoff is 2.1
            entropies.append(getEntropy(freqs))
            highEntropy.write(food + '\n')
            highEntropy.flush()
        else:
            foodGroup = getHighestFreq(freqs)
            entropies.append(getEntropy(freqs))
            number = getNDBNO(foodGroup, data)
            description = getFoodDescription(number)
            output.write(food + ': ' + foodGroup + '; ' + description + '; ' + number + '\n')
            output.flush()
            processed = processed + 1
        time.sleep(2)
    createHistogram(entropies)
    output.write('Percentage of successful cases:' + percentage(processed/total) + '\n')
    output.close()
    notFood.close()
    highEntropy.close()

listNDBNO(getFood())
