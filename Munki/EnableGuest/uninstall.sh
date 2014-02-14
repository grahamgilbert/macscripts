#!/bin/bash

# Disables the Guest User. Script based on https://github.com/sheagcraig/guestAccount/blob/master/guest_account
dscl='/usr/bin/dscl'
security='/usr/bin/security'

$dscl . -delete /Users/Guest
$security delete-generic-password -a Guest -s com.apple.loginwindow.guest-account -D "application password" /Library/Keychains/System.keychain

# Also-do we need this still? (Should un-tick the box)
defaults write /Library/Preferences/com.apple.loginwindow GuestEnabled -bool FALSE

# Doesn't have an effect, but here for reference
#defaults write /Library/Preferences/com.apple.loginwindow DisableGuestAccount -bool TRUE
#defaults write /Library/Preferences/com.apple.loginwindow EnableGuestAccount -bool FALSE

logger -s "$0: Guest account disabled"