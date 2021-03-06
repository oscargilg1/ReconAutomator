
#!/usr/bin/python3
import sys
import subdomainFinder
import shodan
import ipFinder
import urlScan
import waybackmachine
import argparse
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

SHODAN_API_KEY = config.get('api-keys','shodan')
c99_API_KEY = config.get('api-keys','c99')
api_shodan = shodan.Shodan(SHODAN_API_KEY)
chaos_api = config.get('api-keys','chaos')







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
	urlScan.getUrls(target),waybackmachine.getUrls(target)


