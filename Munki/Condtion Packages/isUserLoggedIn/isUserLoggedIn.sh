#!/bin/bash

# This was written by Patrick Fergus and preserved here so I have a chance of finding it again
# https://foigus.wordpress.com/2014/12/15/distributing-dps-desktop-tools-for-indesign-cc-2014-with-munki/

# Extended 18/03/15 by Graham Gilbert to also record the current user

plistLocation=/Library/Managed\ Installs/ConditionalItems

#Verify a user is logged in
loggedInUser=`/usr/bin/python -c 'from SystemConfiguration import SCDynamicStoreCopyConsoleUser; import sys; username = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]; username = [username,""][username in [u"loginwindow", None, u""]]; sys.stdout.write(username + "\n");'`

if [ ! -z "${loggedInUser}" ]
then
  /usr/bin/defaults write "${plistLocation}" isUserLoggedIn -bool true
else
  /usr/bin/defaults write "${plistLocation}" isUserLoggedIn -bool false
fi

if [ ! -z "${loggedInUser}" ]
then
  /usr/bin/defaults write "${plistLocation}" current_user "${loggedInUser}"
else
  /usr/bin/defaults write "${plistLocation}" current_user "no_user_logged_in"
fi