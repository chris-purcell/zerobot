#!/usr/bin/env python

# Import required modules
import requests
from lxml import html

# Describe are function
def ipfinder():
# Set up the variables
    IPADDR='192.168.1.100'
    requests.packages.urllib3.disable_warnings()
    source = requests.get("https://ipfinder.rackspace.com/"+ IPADDR, verify=False).text
    tree = html.fromstring(source)
    ip_info = tree.xpath('//div[@class="row"]/div/p/text()')
    dev_info = tree.xpath('//div[@class="row"]/div/p/a/text()')
    return "IP Address:" + ('%s' % ip_info[0].split(":")[1].split("\n")[0]) + "\n" + \
           "Account: https://core.rackspace.com/py/core/#/account/" + dev_info[0] + "\n" + \
           "Device: https://core.rackspace.com/py/core/#/device/" + dev_info[1]

ipfinder()

