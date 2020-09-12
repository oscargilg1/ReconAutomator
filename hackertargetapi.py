#!/usr/bin/ python3
import requests


class hackertarget():

	def hostsearch(self, target): 
		try:
			r = requests.get("https://api.hackertarget.com/hostsearch/?q=%s" % target)
			r = r.text
			r = r.replace("\n",",") 
			r = r.replace("www.","")
			r = r.split(",") 
			htsubdomains = []
			htIps = []
			for i in range(len(r)): 
				if i % 2 == 0: 
					htsubdomains.append(r[i])
				elif i % 2 != 0:
					htIps.append(r[i])
			return(htsubdomains, htIps) 
		except:
			return("An error occurred.")



	def getIps(self, target):
		try:
			r = requests.get("https://api.hackertarget.com/hostsearch/?q=%s" % target)
			r = r.text
			r = r.replace("\n",",") 
			r = r.split(",") 
			htsubdomains = []
			htIps = []
			for i in range(len(r)): 
				if i % 2 != 0: 
					htIps.append(r[i])
			return(htIps) 
		except:
			return("An error occurred.")





