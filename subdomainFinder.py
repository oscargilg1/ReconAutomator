#!/usr/bin/python3
import c99
import shodanAPI
import hackertargetapi
import chaosAPI
import threading
import json
import waybackmachine

subdomains = []

def startFinder(target, c99_API_KEY, api_shodan, chaos_api):
	c99 = threading.Thread(target=c99Finder, args=(target,c99_API_KEY,))
	c99.start()
	ht = threading.Thread(target=htFinder, args=(target,))
	ht.start()
	Shodan = threading.Thread(target=shodanSearch, args=(target, api_shodan))
	Shodan.start()
	chaos = threading.Thread(target=chaosFinder, args=(target,chaos_api,))
	chaos.start()
	wayback = threading.Thread(target=waybackFinder, args=(target,))
	wayback.start()
	c99.join()
	ht.join()
	Shodan.join()
	chaos.join()
	wayback.join()
	print('\n'.join(subdomains))
	

def c99Finder(target, c99_API_KEY):
	c99subdomains, c99ip = c99.subFinder(target, c99_API_KEY) 
	for i in range(len(c99subdomains)):
		domain = c99subdomains[i]
		if domain not in list(subdomains):
			subdomains.append(domain)


def htFinder(target):
	hackertarget = hackertargetapi.hackertarget()
	htSubdomains, htIp = hackertarget.hostsearch(target)
	for i in range(len(htSubdomains)):
		domain = htSubdomains[i]
		if domain not in list(subdomains):
			subdomains.append(domain)


def shodanSearch(target, api_shodan):
	Subdomains = shodanAPI.shodanapi()
	subs = Subdomains.subfinder(target, api_shodan)
	for i in range(len(subs)):
		domain = json.dumps(subs[i])
		if domain not in list(subdomains):
			subdomains.append(domain)
	
def chaosFinder(target, chaos_api):
	Subdomains = chaosAPI.subFinder(target, chaos_api)
	for i in range(len(Subdomains)):
		subs = Subdomains[i]
		if subs not in subdomains:
			subdomains.append(subs)	


def waybackFinder(target):
	Subs = waybackmachine.getSubs(target)
	
	for i in range(len(Subs)):
		subs = Subs[i]
		if subs not in subdomains:
			subdomains.append(subs)
	