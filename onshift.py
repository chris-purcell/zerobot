#!/usr/bin/env python
# Import required modules
import time, requests
import simplejson as json

# Variables for daily coverage check against staffing calendar
team = "436"
date = time.strftime("%Y-%m-%d")
url = "https://www.staffingcalendar.com/combined/api_dailycoverage.php?"
r = requests.get(url + "Date=" + date + "&team=" + team)
j = r.json()

for k,v in j.iteritems():
    print j[k]['empTitle'],j[k]['firstName'],j[k]['lastName'],j[k]['extension']
