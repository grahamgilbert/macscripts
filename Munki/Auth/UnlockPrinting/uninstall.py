#!/usr/bin/env python

import subprocess
import sys
import plistlib

# Group System Preferences was be opened to
group = 'everyone'

command = ['/usr/bin/security', 'authorizationdb', 'read', 'system.preferences.printing']

task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()
formatted = plistlib.readPlistFromString(out)


originalGroup = 'admin'
# If the group doesn't match, we're going to correct it.
if formatted['group'] != originalGroup:
    formatted['group'] = originalGroup
    # Convert back to plist
    input_plist = plistlib.writePlistToString(formatted)
    # Write the plist back to the authorizationdb
    command = ['/usr/bin/security', 'authorizationdb', 'write', 'system.preferences.printing']
    task = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = task.communicate(input=input_plist)
    

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
groupPresent = False
for pos,item in enumerate(list):
    if item != 'NestedGroups:':
        if item == guid:
            groupPresent = True

# if groupPresent isn't True, then we don't need to uninstall!

if groupPresent == True:
    command = ['/usr/bin/dscl', '/Local/Default', '-delete', '/Groups/lpadmin', 'NestedGroups', guid]
    task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = task.communicate()