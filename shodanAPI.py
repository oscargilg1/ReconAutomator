import shodan
import json


class shodanapi():

    def subfinder(self, target, api_shodan):
        try: 
            query = api_shodan.search("hostname:%s" % target)

            subDomainList = []

            for subdomain in query['matches']:
                subDomainList.append(subdomain['hostnames'])
            return subDomainList     
        
            


        except:
            print("An error occurred")

        if api_shodan is None:
            pass



    def ipFinder(self, target, api_shodan):
        try:

            query = api_shodan.search("hostname:%s" % target)

            ipList = []

            for ip in query['matches']:
                ipList.append(json.dumps(ip['ip_str']))
            return ipList  



        except:
            print("An error occurred")


        if api_shodan is None:
            pass