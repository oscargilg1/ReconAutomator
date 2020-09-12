#!/usr/bin/python3
import json
import requests

target = "creditkarma.com"



def getUrls(target):
	query = requests.get("https://urlscan.io/api/v1/search/?q=domain:%s" % target + "&size=10000")
    
	response = json.loads(query.text)

	extractedFields = response['results']
	
	for i in range(len(extractedFields)):
		myList = extractedFields[i]['task']['url']
		print(json.dumps(myList).replace('"', ""))

    

def getSubs(target):
    ipList = []
    finalList = []
    for i in range(len(response['results'])):
        subs = response['results'][i]['task']['domain']
        if "%s" % target in subs:
            subList.append(subs)


    for i in range(len(subList)):
        sub = subList[i]
        if sub not in finalList:
            finalList.append(sub)


