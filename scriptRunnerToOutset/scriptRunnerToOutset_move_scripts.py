#!/usr/bin/python

import plistlib
import os
import sys
import shutil

# Change this to where your 'once' directory is
scriptrunner_runonce_dir = '/Library/Management/scriptRunner/once'

# Change this to where your 'every' directory is
scriptrunner_runevery_dir = '/Library/Management/scriptRunner/every'

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

def copy_scripts(source, target):
    for script in os.listdir(source):
        old_path = os.path.join(source, script)
        
        extension = get_script_type(old_path)

        if script[-3:] != extension:
            script = script + extension

        target_path = os.path.join(target, script)
        shutil.copyfile(old_path, target_path)

        os.chmod(target_path,0755)


def main():

    outset_runonce_dir = '/usr/local/outset/login-once'
    outset_runevery_dir = '/usr/local/outset/login-every'
    if os.path.exists(scriptrunner_runonce_dir):
        copy_scripts(scriptrunner_runonce_dir, outset_runonce_dir)
    if os.path.exists(scriptrunner_runevery_dir):
        copy_scripts(scriptrunner_runevery_dir, outset_runevery_dir)

if __name__ == '__main__':
  main()