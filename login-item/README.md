login-item
========

This package will set an application to be a login item for new and exisitng users.

It requires [The Luggage](https://github.com/unixorn/luggage) to build the package.

##Configuration
Open theLoginItem in your favourite editor and edit the line below to point to the path of the app you want to put into the user's login items.

	make login item at end with properties {path:"/Applications/Something.app", kind:application}
	
##What's happening
We pop theLoginItem (the script that does the real work) in /usr/local/management, and then loop over all the user's with home directories in /Users (thus avoiding our management account with it's home in /var) putting a LaunchAgent in each user's home. We then put the LaunchAgent in the default user template. The script will delete the LaunchAgent after it has run, so it will only set the Login Item once.