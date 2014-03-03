#!/bin/sh
/usr/sbin/jamf -removeFramework

# We configured without profiles with Casper, so clean up here
rm /Library/Preferences/ManagedInstalls.plist