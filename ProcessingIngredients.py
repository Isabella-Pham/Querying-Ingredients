from Querying import * #import file with functions to get NDBNO
import time

def getFood():
    with open ("list.txt", "r") as file:
        list = file.read().splitlines()
    return list

def percentage(processed, total): #returns the percentage of ingredients that do not need to be manually processed
    return (processed/total)*100 + '%'

def listNDBNO(list): #returns a dictionary of the food and it's NDBNO number
    NDBNOs = {};
    manually = [];
    total = 0;
    processed = 0;
    for food in list:
        data = get_api(food)
        if data == 'ERROR':
            manually.append(food)
            continue
        freqs = getFrequencies(data)
        if bool(freqs) == False:
            continue
        foodGroup = getHighestFreq(freqs)
        if isEntropyLow(freqs):
            manually.append(food)
        else:
            number = getNDBNO(foodGroup, data);
            NDBNOs[food] = number
            processed += 1
        total += 1
        time.sleep(5)
    print(percentage(processed/total))
    f = open('Output.txt', 'w')
    f.write('Below is a list of foods and their NDBNO numbers')
    for food in NBDNOs:
        f.write(food + ':' + NBDNOs[food] + '\n');
    m = open('Manual.txt', 'w')
    m.write('Below is a list of foods that must be manually checked')
    for food in manually:
        m.write(food + '\n')

listNDBNO(getFood())
