import json
import requests

def subFinder(target, chaos_api):
    subList = []
    query = requests.get("https://dns.projectdiscovery.io/dns/%s/subdomains" % target, headers={"Authorization":"%s" % chaos_api})

    response = query.json()


    for i in response['subdomains']:
        subs = i.replace("www.", "") + "." + target
        if subs not in subList:
            subList.append(subs)
        return subList