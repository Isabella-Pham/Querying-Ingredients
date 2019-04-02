import requests
import json
import os
import time
import urllib

def getFood():
    with open ("list.txt", "r") as f: #insert name of file you're getting list of foods from
        l = f.read().splitlines()
    return l

url = 'https://trackapi.nutritionix.com/v2/natural/tags'
headers = {'Content-Type': 'application/json',
           "x-app-id": "240c70ea", 'x-app-key': '5b98e8dfb93416ccf82a05f5f5073f72', 'x-remote-user-id': '0'}


data = '{ \"num_servings\": 1,\"query\": \"mango\",  \"aggregate\": \"string\",  \"line_delimited\": false,  \"use_raw_foods\": true,  \"include_subrecipe\": false,  \"timezone\": \"US\/ Eastern\",  \"consumed_at\": null,  \"lat\": 0,  \"lng\": 0,  \"meal_type\": 0,  \"use_branded_foods\": true,  \"locale\": \"en_US\"}'
json_data = json.loads(data)
l=getFood()

# remember we are limited to 2*500 queries a day, Isabella you have an offset 1229
outfile = open('tempCoversionTables.txt', 'w') #file results are being written into
'''
for line in l:
    if(line.split()[1].isdigit()):
        NDBNO = line.split()[1]
        url1 = 'https://api.nal.usda.gov/ndb/reports/?ndbno=' + NDBNO + '&type=f&format=json&api_key=adBdNNK4tcs1RKpEOJnb6If4pZ9YH1B75ii9roZS'
        with urllib.request.urlopen(url1) as url1:
            data = json.loads(url1.read().decode())
        name =  data['report']['food']['name']
        json_data["query"] = name
    	#headers['x-remote-user-id']=str(i%2)
    	#print("Request:\n\n"+json.dumps(json_data, indent=2, sort_keys=True))
        response = requests.post(url, data=json.dumps(json_data), headers=headers)
    	#write this to a file
        parsed = json.loads(response.text)
    	# not food or no result
        if 'message' in parsed:
            outfile.write(line.split()[0]+'\t0\t'+response.text+'\n')
        else:
            outfile.write(line.split()[0]+'\t'+str(len(parsed))+'\t'+response.text+'\n')
        outfile.flush()
    else:
        outfile.write(line + "\n")
        outfile.flush()
    time.sleep(10)
outfile.close()
'''
for i in l:
	# way to change query
	print(i)
	json_data["query"] = i
	#headers['x-remote-user-id']=str(i%2)
	#print("Request:\n\n"+json.dumps(json_data, indent=2, sort_keys=True))
	response = requests.post(url, data=json.dumps(json_data), headers=headers)
	#write this to a file
	parsed = json.loads(response.text)
	# not food or no result
	if 'message' in parsed:
		outfile.write(i+'\t0\t'+response.text+'\n')
	else:
		outfile.write(i+'\t'+str(len(parsed))+'\t'+response.text+'\n')
	outfile.flush()
	time.sleep(10)
outfile.close()
#response_json = json.dumps(parsed, indent=2, sort_keys=True)
#print("\n\nResponse:\n\n"+response_json)


def getMultipleResults():
    with open ("nutritionix.txt", "r") as f:
        l = f.read().splitlines()
    outfile = open('multipleResults.txt', 'w')
    for line in l:
        numResults = line.split()[1]
        if int(numResults) > 1:
            outfile.write(line + "\n")
            outfile.flush()
    outfile.close()
def getNoResults():
    with open ("nutritionix.txt", "r") as f:
        l = f.read().splitlines()
    outfile = open('noResults.txt', 'w')
    for line in l:
        numResults = line.split()[1]
        if int(numResults) == 0:
            outfile.write(line.split()[0] + "\n")
            outfile.flush()
    outfile.close()
def noResultsConverstionTable():
    with open ("noResults.txt", "r") as f:
        l = f.read().splitlines()
    outfile = open('noResultsConversionTables.txt', 'w')
    for line in l:
        if(line.split()[1].isdigit()):
            NDBNO = line.split()[1]
            url = 'https://api.nal.usda.gov/ndb/reports/?ndbno=' + NDBNO + '&type=f&format=json&api_key=adBdNNK4tcs1RKpEOJnb6If4pZ9YH1B75ii9roZS'
            with urllib.request.urlopen(url) as url:
                data = json.loads(url.read().decode())
            name =  data['report']['food']['name']
        else:
            outfile.write(line + "\n")
            outfile.flush()
    outfile.close()
