#!/usr/bin/python

import subprocess
import sys
import plistlib

# Group System Preferences should be opened to
group = 'admin'

# Get the OS Version
command = ['/usr/bin/sw_vers', '-productVersion']
task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()

groups = out.split('.')

v = groups[0].strip() + '.' + groups[1].strip()

command = ['/usr/bin/security', 'authorizationdb', 'read', 'system.services.systemconfiguration.network']

task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()
formatted = plistlib.readPlistFromString(out)

# If we're on 10.9 and the group doesn't match, we're going to correct it.
if v == '10.9' or v == '10.10':
    if formatted['group'] != group:
        formatted['group'] = group
        # Convert back to plist
        input_plist = plistlib.writePlistToString(formatted)
        # Write the plist back to the authorizationdb
        command = ['/usr/bin/security', 'authorizationdb', 'write', 'system.services.systemconfiguration.network']
        task = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out, err) = task.communicate(input=input_plist)

# If we're on 10.8 and the rule doesn't match, we're going to correct it.
if v == '10.8':
    if formatted['rule'] != 'root-or-entitled-admin-or-app-specific-admin':
        formatted['rule'] = 'root-or-entitled-admin-or-app-specific-admin'
        # Convert back to plist
        input_plist = plistlib.writePlistToString(formatted)
        # Write the plist back to the authorizationdb
        command = ['/usr/bin/security', 'authorizationdb', 'write', 'system.services.systemconfiguration.network']
        task = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out, err) = task.communicate(input=input_plist) 

command = ['/usr/bin/security', 'authorizationdb', 'read', 'system.preferences.network']

task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()
formatted = plistlib.readPlistFromString(out)

# If the group doesn't match, we're going to correct it.
if formatted['group'] != group:
    formatted['group'] = group
    # Convert back to plist
    input_plist = plistlib.writePlistToString(formatted)
    # Write the plist back to the authorizationdb
    command = ['/usr/bin/security', 'authorizationdb', 'write', 'system.preferences.network']
    task = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = task.communicate(input=input_plist)