#!/usr/bin/env python
# Import required modules
import time, requests
import simplejson as json

# Variables for daily coverage check against staffing calendar
def onshift():
    team = "436"
    date = time.strftime("%Y-%m-%d")
    url = "https://www.staffingcalendar.com/combined/api_dailycoverage.php?"
    r = requests.get(url + "Date=" + date + "&team=" + team)
    j = r.json()
    j = j.values()
    j = sorted(j, key=lambda s: s['empTitle'], reverse=True)
    data = []
    for i in range(len(j)):
        data.append(j[i]['firstName'] + " ")
        data.append(j[i]['lastName'] + ", ")
        data.append(j[i]['empTitle'] + ", ")
        data.append(j[i]['extension'] + "\n")
    return 'Workers in the office:\n' + (''.join('{}'.format(k) for i,k in enumerate(data)))
