#!/usr/bin/env python

import subprocess
import sys
import plistlib

# Group Date and Time  System Preferences should be opened to
group = 'everyone'

command = ['/usr/bin/security', 'authorizationdb', 'read', 'system.preferences.datetime']

task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()

formatted = plistlib.readPlistFromString(out)
# if group matches, exit 1 as we don't need to install
if formatted['group'] == group:
    sys.exit(1)
else:
    # if it doesn't we're exiting with 0 as we need to perform the install
    sys.exit(0)