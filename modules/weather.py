import requests
import lxml.etree as ET

def weather():
    result = requests.get("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=0&locCode=78239")
    result.status_code
    c = result.content
    doc = ET.fromstring(c)
    for item in doc.xpath('//item'):
        for elt in item.xpath('descendant::*'):
            if "Currently:" in ET.tostring(elt):
                str = ET.tostring(elt)
                str = str.replace('<title>Currently: ','')
                str = str.replace('</title>','')
                return "The weather is currently " + str
