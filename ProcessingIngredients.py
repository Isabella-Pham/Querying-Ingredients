from Querying import * #import file with functions to get NDBNO
import time

def getFood():
    with open ("list.txt", "r") as file:
        list = file.read().splitlines()
    return list

def percentage(processed, total): #returns the percentage of ingredients that do not need to be manually processed
    return (processed/total)*100 + '%'

def listNDBNO(list): #returns a dictionary of the food and it's NDBNO number
    #NDBNOs = {};
    #manually = [];
    total = 0;
    processed = 0;
    f = open('Output.txt', 'w')
    m = open('Manual.txt', 'w')
    f.write('Below is a list of foods and their NDBNO numbers')
    m.write('Below is a list of foods that must be manually checked')
    for food in list:
        total = total + 1
        data = get_api(food)
        if data == 'ERROR':
            m.write(food + '\n')
            #manually.append(food)
            continue
        freqs = getFrequencies(data)
        if bool(freqs) == False:
            continue
        foodGroup = getHighestFreq(freqs)
        if isEntropyLow(freqs):
            #manually.append(food)
            m.write(food + '\n')
        else:
            number = getNDBNO(foodGroup, data);
            #NDBNOs[food] = number
            f.write(food + ':' + number + '\n');
            processed = processed + 1
        time.sleep(10)
    f.write('Percentage of successful cases:' + percentage(processed/total))
    f.close()
    m.close()

listNDBNO(getFood())
