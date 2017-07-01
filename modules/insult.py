#!/usr/bin/env python

# Import required module
from random import choice

# List of choices
insults = [
    "asshat",
    "dickwit",
    "cockwomble",
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
    return "@user is a total %s" % getRandomInsult()
