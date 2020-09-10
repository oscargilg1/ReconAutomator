
import sys
from os import system, name
from time import sleep
import subdomainFinder
import shodan
import ipFinder
import urlScan
import argparse

SHODAN_API_KEY = ""
c99_API_KEY = ""
api_shodan = shodan.Shodan(SHODAN_API_KEY)
chaos_api = ""







parser = argparse.ArgumentParser()
parser.add_argument("target.com", help="Your target ex: google.com")
parser.add_argument("-s", "--subdomains", action="store_true",
                    help="Get a list of subdomains")
parser.add_argument("-i", "--ips", action="store_true",
                    help="Get a list of IP addresses")
parser.add_argument("-u", "--urls", action="store_true",
                    help="Get a list of urls for given target")


args = parser.parse_args()
target = sys.argv[1]
if args.subdomains:
    subdomainFinder.startFinder(target, c99_API_KEY, api_shodan, chaos_api)
if args.ips:
	ipFinder.startFinder(target, c99_API_KEY, api_shodan)
if args.urls:
	urlScan.getUrls(target)


