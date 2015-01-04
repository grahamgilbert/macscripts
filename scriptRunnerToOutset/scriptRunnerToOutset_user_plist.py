#!/usr/bin/python

import plistlib
import os
import sys

# Change this to where your 'once' directory is
scriptrunner_runonce_dir = '/Library/Management/scriptRunner/once'

# This is the default - change this line if you're saving your preferences elsewhere
scriptrunner_plist = os.path.expanduser('~/Library/Preferences/com.company.scriptrunner.plist')

def get_script_type(path):
    try:
        with open(path, 'r') as f:
            first_line = f.readline()
    except (OSError, IOError) as e:
        # assume it's a shell script
        print "Couldn't read script, reverting to default of shell"
        return ".sh"

    # Make sure it's actually a shebang
    if first_line[3:] == '#!/':
        # is it bash or sh?
        if "sh" in first_line:
            return ".sh"

        # Python?
        if "python" in first_line:
            return ".py"

        # Ruby?
        if "ruby" in first_line:
            return ".rb"
    else:
        return ".sh"

def main():
    outset_plist = os.path.expanduser('~/Library/Preferences/com.github.outset.once.plist')

    outset_runonce_dir = '/usr/local/outset/login-once'

    try:
        scriptrunner = plistlib.readPlist(scriptrunner_plist)
    except IOError:
        # There isn't a scriptrunner plsit, no point carrying on
        sys.exit(0)

    try:
        d = plistlib.readPlist(outset_plist)
    except IOError:
        d = {}

    if os.path.exists(scriptrunner_runonce_dir):

        for script, date in scriptrunner.iteritems():
            extension = get_script_type(os.path.join(scriptrunner_runonce_dir,script))

            if script[-3:] != extension:
                script = script + extension
            outset_path = os.path.join(outset_runonce_dir, script)
            d[outset_path] = date

        plistlib.writePlist(d, outset_plist)

if __name__ == '__main__':
  main()

# key is /usr/local/outset/login-once/scriptname
# date = date