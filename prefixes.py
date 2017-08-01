#!/usr/bin/env python

# List of choices
codes = [
    "501 San Antonio (SAT)",
    "503 Austin (ATX)",
    "504 Dallas (DFW)",
    "507 Virginia (IAD)",
    "508 London (LON)",
    "509 Hong Kong (HKG)",
    "515 Sydney (SYD)",
    "700 US Hunt Group",
    "720 International Hunt Group"
]

# Create function
def prefixes():
    return 'Office Prefixes:\n' + ('\n'.join('{}'.format(k) for i,k in enumerate(codes)))
