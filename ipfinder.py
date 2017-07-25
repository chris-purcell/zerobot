#!/usr/bin/env python

# Import required modules
import requests
from lxml import html

# Describe are function
def ipfinder():
# Set up the variables
    IPADDR='192.168.1.100'
    source = requests.get("https://ipfinder.rackspace.com/" + IPADDR, verify=False).text
    tree = html.fromstring(source)
    ip_info = tree.xpath('//div[@class="row"]/div/p/text()')
    dev_info = tree.xpath('//div[@class="row"]/div/p/a/text()')
    return ("IP Address:" + ('%s' % ip_info[0].split(":")[1].split("\n")[0]) + "\n" + "Account: " \
            + dev_info[0] + "\n" + "Device: " + dev_info[1])

