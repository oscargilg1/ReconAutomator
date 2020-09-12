#!/usr/bin/python3
import c99
import shodanAPI
import hackertargetapi
import threading
import json

ipList = []

def startFinder(target, c99_API_KEY, api_shodan):
	c99 = threading.Thread(target=c99Finder, args=(target,c99_API_KEY,))
	c99.start()
	ht = threading.Thread(target=htFinder, args=(target,))
	ht.start()
	Shodan = threading.Thread(target=shodanSearch, args=(target, api_shodan))
	Shodan.start()
	c99.join()
	ht.join()
	Shodan.join()
	print('\n'.join(map(str, ipList)).replace('"', "")) 

def c99Finder(target, c99_API_KEY):
	c99ip = c99.ipFinder(target, c99_API_KEY)
	for i in range(len(c99ip)):
		ips = c99ip[i]
		if ips not in list(ipList):
			ipList.append(ips)

def htFinder(target):
	hackertarget = hackertargetapi.hackertarget()
	htIp = hackertarget.getIps(target)
	for i in range(len(htIp)):
		ips = htIp[i]
		if ips not in list(ipList):
			ipList.append(ips)

def shodanSearch(target, api_shodan):
	getIp = shodanAPI.shodanapi()
	ip = getIp.ipFinder(target, api_shodan)
	for i in range(len(ip)):
		ips = ip[i]
		if ips not in list(ipList):
			ipList.append(ips)


	
