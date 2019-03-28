import requests
import json
import os
import time

'''
def getFood():
    with open ("list.txt", "r") as f:
        l = f.read().splitlines()
    return l

url = 'https://trackapi.nutritionix.com/v2/natural/tags'
headers = {'Content-Type': 'application/json',
           "x-app-id": "240c70ea", 'x-app-key': '5b98e8dfb93416ccf82a05f5f5073f72', 'x-remote-user-id': '0'}


data = '{ \"num_servings\": 1,\"query\": \"mango\",  \"aggregate\": \"string\",  \"line_delimited\": false,  \"use_raw_foods\": false,  \"include_subrecipe\": false,  \"timezone\": \"US\/ Eastern\",  \"consumed_at\": null,  \"lat\": 0,  \"lng\": 0,  \"meal_type\": 0,  \"use_branded_foods\": false,  \"locale\": \"en_US\"}'

json_data = json.loads(data)
outfile=open('nutritionix.txt','w')
l=getFood()


# remember we are limited to 2*500 queries a day, Isabella you have an offset 1229
for i in l[1229:]:
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
'''

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

getNoResults()
