#!/usr/bin/env python

# Import required module
from random import choice

# List of choices
insults = [
    "Bedswerver",
    "Cumberworld",
    "Fopdoodle",
    "Tosser",
    "Wanker",
    "Daft cow",
    "Barmy",
    "Minger",
    "Muppet",
    "Nutter",
    "Plonker",
    "Knob head",
    "Maggot"
]

# Create function
def insult():
    return choice(insults) + "!"
