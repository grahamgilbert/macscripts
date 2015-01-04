#!/usr/bin/python
#
#    Checks if a Puppet Run has happened in the last month. If not, it will
#    install a package that will re-enroll the Mac

import sys
sys.path.append('/usr/local/sal')

import yaml
import os
from datetime import datetime, timedelta, date

today = date.today()
month_ago = today - timedelta(days=30)
try:
    f = open('/var/lib/puppet/state/last_run_summary.yaml', 'r')
    puppetreport = yaml.load(f.read())
    last_run = date.fromtimestamp(float(puppetreport['time']['last_run']))
    if last_run < month_ago:
        sys.exit(0)
    else:
        sys.exit(1)
except:
    # The last run summary isn't there, assume it's never run, need to bootstrap
    sys.exit(0)