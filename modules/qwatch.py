#!/usr/bin/env python
# Import required modules
import requests, time
from bs4 import BeautifulSoup

def qwatch():
    data = []
    source = requests.get("http://qwatch.it.rackspace.com").text
    soup = BeautifulSoup(source, 'html.parser')
    for link in soup.find_all('a'):
        if 'ticket' in link.get('href'):
            data.append(link.get('href'))
    return "Pending SLA Violation tickets:\n" + ('\n'.join('{}'.format(k) for i,k in enumerate(data)))
