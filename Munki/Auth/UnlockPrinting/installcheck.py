#!/usr/bin/env python

import subprocess
import sys
import plistlib

# Group Printing System Preferences should be opened to
group = 'everyone'

command = ['/usr/bin/security', 'authorizationdb', 'read', 'system.preferences.printing']

task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()

formatted = plistlib.readPlistFromString(out)

# Get all of the groups nested under lpadmin
command = ['/usr/bin/dscl', '/Local/Default', 'read', '/Groups/lpadmin', 'NestedGroups']
task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()

list = out.strip().split(" ")

# Get the GUID of the desired group

command = ['/usr/bin/dscl', '/Local/Default', 'read', '/Groups/'+group, 'GeneratedUID']
task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()
guid = out.strip().replace('GeneratedUID: ', '')

# Iterate over all of the groups, if one of them is the specified group, we this part doesn't need to be installed.
for pos,item in enumerate(list):
    if item != 'NestedGroups:':
        if item == guid:
            groupPresent = True

# if group matches, exit 1 as we don't need to install
if formatted['group'] == group and groupPresent == True:
    sys.exit(1)
else:
    # if it doesn't we're exiting with 0 as we need to perform the install
    sys.exit(0)