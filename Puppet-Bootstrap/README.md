Puppet-Bootstrap
========

This is an example of a package that pulls it's main payload from a remote source. See this post on my blog for more information on the reasons you might want to use something like this.

This particular package will connect a Mac OS X client to a Puppet Master.

It requires [The Luggage](https://github.com/unixorn/luggage) to build the package.

##Configuration

Open up puppet_bootstrap and edit the address of the Puppet Server to match your own environment and add the flags required to the puppet_install.py script.
##What's happening
We pop theLoginItem (the script that does the real work) in /usr/local/management, and then loop over all the user's with home directories in /Users (thus avoiding our management account with it's home in /var) putting a LaunchAgent in each user's home. We then put the LaunchAgent in the default user template. The script will delete the LaunchAgent after it has run, so it will only set the Login Item once.