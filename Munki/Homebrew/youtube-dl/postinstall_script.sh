#!/bin/bash

CURRENT_USER=`/bin/ls -l /dev/console | /usr/bin/awk '{ print $3 }'`

if [ "$CURRENT_USER" == 'root' ]; then
    # this can't run at the login window, we need the current user
    exit 1
fi

chown $CURRENT_USER /usr/local
mkdir -p /usr/local/etc
chown $CURRENT_USER /usr/local/etc
mkdir -p /usr/local/bin
chown -R $CURRENT_USER /usr/local/bin
mkdir -p /usr/local/share/man
chown -R $CURRENT_USER /usr/local/share/man

#download and install youtube-dl
su $CURRENT_USER -c "/usr/local/bin/brew install youtube-dl"