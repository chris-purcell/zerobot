#!/usr/bin/env python

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
