#!/bin/bash

CURRENT_USER=`/bin/ls -l /dev/console | /usr/bin/awk '{ print $3 }'`

if [ "$CURRENT_USER" == 'root' ]; then
    # this can't run at the login window, we need the current user
    exit 1
fi

mkdir -p /usr/local
mkdir -p /usr/local/homebrew
mkdir -p /usr/local/bin
chown $CURRENT_USER:_developer /usr/local/homebrew
chown $CURRENT_USER:_developer /usr/local/bin

#download and install homebrew
su $CURRENT_USER -c "/bin/bash -o pipefail -c '/usr/bin/curl -skSfL https://github.com/mxcl/homebrew/tarball/master | (cd /usr/local ; /usr/bin/tar xz -m --strip 1 -C homebrew; ln -s /usr/local/homebrew/bin/brew /usr/local/bin/brew)'"