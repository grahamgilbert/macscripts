#!/usr/bin/python

import subprocess
import sys
import plistlib

# Group System Preferences should be opened to
group = 'everyone'

# Get the OS Version
command = ['/usr/bin/sw_vers', '-productVersion']
task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()

groups = out.split('.')

v = groups[0].strip() + '.' + groups[1].strip()

command = ['/usr/bin/security', 'authorizationdb', 'read', 'system.preferences.network']

task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()

formatted = plistlib.readPlistFromString(out)

command = ['/usr/bin/security', 'authorizationdb', 'read', 'system.services.systemconfiguration.network']

task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()

formatted2 = plistlib.readPlistFromString(out)

# Need to check the group for 10.9, and the rule for 10.8
# if group matches for both rights, exit 1 as we don't need to install
if v == '10.9' or v == '10.10':  
    try:
        # There are two formats for this plist. WAT?
        if formatted['group'] == group and formatted2['group'] == group:
            sys.exit(1)
        else:
            # if it doesn't we're exiting with 0 as we need to perform the install
            sys.exit(0)
    except:
        # the group might not be set, let's do it
        sys.exit(0)
 
if v == '10.8':
    if formatted['group'] == group and formatted2['rule'] == 'allow':
        sys.exit(1)
    else:
        # if it doesn't we're exiting with 0 as we need to perform the install
        sys.exit(0)