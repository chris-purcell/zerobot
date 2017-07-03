#!/usr/bin/env python

# List of choices
codes = [
    "01 Tickets\n",
    "02 Break\n",
    "03 Lunch\n",
    "04 Meeting\n",
    "05 Assist\n",
    "06 Training\n",
    "07 Project\n",
    "08 Maintenance\n",
    "09 Chat\n"
]

# Create function
def auxcodes():
    return 'Aux Codes:\n' + ('\n'.join('{}'.format(k) for i,k in enumerate(codes)))
