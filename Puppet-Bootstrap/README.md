Puppet-Bootstrap
========

This is an example of a package that pulls it's main payload from a remote source. See this post on my blog for more information on the reasons you might want to use something like this.

This particular package will connect a Mac OS X client to a Puppet Master.

It requires [The Luggage](https://github.com/unixorn/luggage) to build the package.

##Configuration

Open up puppet_bootstrap and edit the address of the Puppet Server to match your own environment and add the flags required to the puppet_install.py script.
##What's happening
We pop puppet_bootstrap (the script that does the real work) in /usr/local/puppet_bootstrap. This then runs at boot, and downloads the latest version of the real bootstrap script.