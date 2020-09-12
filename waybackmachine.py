#!/usr/bin/python3

import requests
import json
import urllib3
from urllib.parse import urlparse



def getUrls(target):
    sanitizedUrls = []
    query = requests.get("http://web.archive.org/cdx/search/cdx?url=*.%s&output=json&fl=original&collapse=urlkey" % target)

    response = query.json()
    for i in range(len(response)):
        urlList = []
        urlList.append(response[i])
        urls = '\n'.join(map(str, urlList)).replace("['", "").replace("']", "").replace("www.", "").replace(":80", "")
        sanitizedUrls.append(urls)
    
    return sanitizedUrls

def getSubs(target):
    
    subs = []
    urls = getUrls(target)

    for i in range(len(urls)):
        domain = urlparse(urls[i]).netloc
        if domain not in list(subs):
            subs.append(domain)
    while("" in subs):
        subs.remove("")        
    return subs

    

    