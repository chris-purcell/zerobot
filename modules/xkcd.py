import requests
import random
from lxml import html

def xkcd():
    # Return random XKCD comic for the chat room
    source = requests.get("http://xkcd.com/%d" % random.randint(1,1446)).text
    tree = html.fromstring(source.encode('utf-8'))
    img = tree.xpath('//div[@id="comic"]/img/@src')
    img = img[0]
    return "http:" + img
