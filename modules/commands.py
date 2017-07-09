#!/usr/bin/env python
# Import required modules
import os

# Get list of available commands on startup, by parsing the modules directory
def commands():
    data = []
    path = os.getcwd()
    filenames = os.listdir(path + "/modules/")
    for filename in filenames:
        if filename.endswith('.py') and not filename.startswith("_"):
            filename = filename.split('.')[0]
            data.append("!" + filename)
            data.sort()
    return 'Available commands are:\n' + ('\n'.join('{}'.format(k) for i,k in enumerate(data)))
