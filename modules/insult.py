#!/usr/bin/env python

# Import required module
from random import choice

# List of choices
insults = [
    "bedswerver",
    "cumberworld",
    "fopdoodle",
    "tosser",
    "wanker",
    "daft cow",
    "barmy",
    "minger",
    "muppet",
    "nutter",
    "plonker",
    "arsehole",
    "knob head",
    "maggot"
]

# Create function
def getRandomInsult():
    return choice(insults)

def insult():
    text = ''
    if text and len(text) > 0:
        insulter = text.split()[0]
        print "Insulter: " + insulter
        insultee = text.split()[2]
        print "Insultee: " + insultee
        user = text.strip('!insult ')
        print user
        return "%s is a total %s" % (user,getRandomInsult())
    else:
        return getRandomInsult()
