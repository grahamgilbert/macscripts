#!/usr/bin/python

import sys
import subprocess
'''
Enables Network Time on OS X
'''
command = ['systemsetup', '-getusingnetworktime']

task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()

if out.strip() == 'Network Time: Off':
    command = ['systemsetup', '-setusingnetworktime', 'on']

    task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = task.communicate()