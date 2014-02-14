#!/bin/bash

# Enables the Guest User based on OS version. Script based on https://github.com/sheagcraig/guestAccount/blob/master/guest_account

dscl='/usr/bin/dscl'
security='/usr/bin/security'

# Does guest already exist?
if [ -f /var/db/dslocal/nodes/Default/users/Guest.plist ]; then
	echo "Guest already created!"
	exit 0
else
	# Lion+ has a different procedure for enabling the guest account
	if [ "$(sw_vers | grep -o '10\.6')" != "" ]; then
		logger -s "$0: Not implemented"

		exit 0
	fi

	# Lion+ procedure
	if [ "$(sw_vers | grep -o '10\.[7-9]')" != "" ]; then
		logger "$0: Enabling 10.7/10.8/10.9 Guest"
		$dscl . -create /Users/Guest
		$dscl . -create /Users/Guest dsAttrTypeNative:_defaultLanguage en
		$dscl . -create /Users/Guest dsAttrTypeNative:_guest true
		$dscl . -create /Users/Guest dsAttrTypeNative:_writers__defaultLanguage Guest
		$dscl . -create /Users/Guest dsAttrTypeNative:_writers__LinkedIdentity Guest
		$dscl . -create /Users/Guest dsAttrTypeNative:_writers__UserCertificate Guest
		$dscl . -create /Users/Guest AuthenticationHint ''
		$dscl . -create /Users/Guest NFSHomeDirectory /Users/Guest

		# Give a little extra time for the password and kerberos to play nicely
		sleep 2
		$dscl . -passwd /Users/Guest ''
		sleep 2

		$dscl . -create /Users/Guest Picture "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/UserIcon.icns"
		$dscl . -create /Users/Guest PrimaryGroupID 600
		$dscl . -create /Users/Guest RealName "Guest User"
		$dscl . -create /Users/Guest RecordName Guest
		$dscl . -create /Users/Guest UniqueID 600
		$dscl . -create /Users/Guest UserShell /bin/bash
		$security add-generic-password -a Guest -s com.apple.loginwindow.guest-account -D "application password" /Library/Keychains/System.keychain

		# This seems to be technically unnecessary; it controls whether the "Allow 
		# guests to log in to this computer" checkbox is enabled in SysPrefs 
		defaults write /Library/Preferences/com.apple.loginwindow GuestEnabled -bool TRUE

		# Profiles created with PM have these two keys, but they don't seem to do 
		# anything 
		#defaults write /Library/Preferences/com.apple.loginwindow DisableGuestAccount -bool FALSE
		#defaults write /Library/Preferences/com.apple.loginwindow EnableGuestAccount -bool TRUE

		logger -s "$0: Guest created"

		exit 0
	fi
fi