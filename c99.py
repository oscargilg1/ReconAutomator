import requests
import json

def subFinder(target, c99_API_KEY):
    ipList = []
    finalList = []
    query = requests.get("https://api.c99.nl/subdomainfinder?key=%s" % c99_API_KEY + "&domain=%s" % target + "&json")
    response = json.loads(query.text)
    extractedFields = response['subdomains']

    for i in range(len(extractedFields)):
    	subdomains = str(extractedFields[i]['subdomain'])
    	subdomains = subdomains.replace('www.', '')
    	if subdomains != 'none' and subdomains not in list(finalList):
            finalList.append(subdomains)

    for i in range(len(extractedFields)):
        ipAddr = extractedFields[i]['ip']
        if ipAddr != "none" and ipAddr not in list(ipList):
            ipList.append(ipAddr)
    return(finalList,ipList)

def ipFinder(target, c99_API_KEY):
    return subFinder(target, c99_API_KEY)[1]