#!/usr/bin/python

import sys
import subprocess
'''
Enables Network Time on OS X
'''
command = ['systemsetup', '-getusingnetworktime']

task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()

# if already enabled, exit 1 as we don't need to install
if out.strip() == 'Network Time: On':
    sys.exit(1)
else:
    # if it doesn't we're exiting with 0 as we need to perform the install
    sys.exit(0)