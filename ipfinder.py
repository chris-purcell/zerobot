#!/usr/bin/env python
"""
# Import required modules
import requests
from lxml import html

# Describe are function
def ipfinder():
# Set up the variables
    source = requests.get("https://ipfinder.rackspace.com/192.168.1.100", verify=False).text
    tree = html.fromstring(source)
    ip_info = tree.xpath('//div[@class="row"]/div/p/text()')
    dev_info = tree.xpath('//div[@class="row"]/div/p/a/text()')
    # Display the requisite info!
    #print "IP Address:" + ('%s' % ip_info[0].split(":")[1].split("\n")[0])
    #print "Account: " + dev_info[0]
    #print "Device: " + dev_info[1]
    return ("IP Address:" + ('%s' % ip_info[0].split(":")[1].split("\n")[0]) + "\n" + "Account: " \
            + dev_info[0] + "\n" + "Device: " + dev_info[1])

#!/usr/bin/env python
"""
# ipfinder is a simple python script that utilises the https://ipfinder.rackspace.com/json/ endpoint to search for an IP address.
# This tool is intented for internal RS use only.

import sys
import argparse
import requests
import json
import urllib

# Fixed endpoints
ipfinder_endpoint = 'https://ipfinder.rackspace.com/json/'

# Do not change anything below this line #

parser = argparse.ArgumentParser()
parser.add_argument('ip', metavar='ip_address', type=str, nargs=1, help='an IP address to search')

args = parser.parse_args()

ip = urllib.quote_plus(sys.argv[1]) #URL encode the argument from the command line
url = ipfinder_endpoint+ip

print "\n>> Looking for " + ip

r = requests.get(url,verify=False)

print ">> The returned status code was: " + str(r.status_code) + "\n"

if r.status_code == 400:
    print "This is not a valid IP address!\n"
    exit()
elif r.status_code == 200:
    if not r.json():
        print "IP not found!\n"
        exit()
    else:
        j = r.json()
        print "Device: " + j['device']
        print "Account: " + j['account']
        print "Account type: " + j['account_type']
        print "Source: " + j['source']
        print "Region: " + j['region']
        print "Device URL: " + j['device_url']
        print "Account URL: " + j['account_url']

print
exit()

