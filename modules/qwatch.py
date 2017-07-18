#!/usr/bin/env python
# Import required modules
import requests, time
from bs4 import BeautifulSoup
def qwatch():
    channel = '#zerobot'
    while True:
        data = []
        source = requests.get("http://qwatch.it.rackspace.com").text
        soup = BeautifulSoup(source, 'html.parser')
        table = soup.find('table')
        x = (len(table.find_all('tr')))

        for row in table.find_all('tr')[1:x]:
            col = row.find_all('td')
            name = col[0].getText()
            ticket = 'https://core.rackspace.com/ticket/' + col[1].getText() + "\n"
            if 'windows' in name:
                pass
            else:
                data.append(name.capitalize())
                data.append(ticket)
        return "Pending SLA Violation tickets:\n" + (' '.join('{}'.format(k) for i,k in enumerate(data)))
