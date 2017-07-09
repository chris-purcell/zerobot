#!/usr/bin/env python

# List of choices
codes = [
    "01 Tickets",
    "02 Break",
    "03 Lunch",
    "04 Meeting",
    "05 Assist",
    "06 Training",
    "07 Project",
    "08 Maintenance",
    "09 Chat"
]

# Create function
def auxcodes():
    return 'Aux Codes:\n' + ('\n'.join('{}'.format(k) for i,k in enumerate(codes)))
