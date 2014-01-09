# install_puppet.py

## Overview

This script will download version 3.4.2 of Puppet and 1.7.4 of Facter and install them on a Mac OS X client.

## Options

The following options can be passed to the script:

* ``--server`` - The url of your Puppet Master (will be written to ``/etc/puppet/puppet.conf``). Defaults to puppet.grahamgilbert.dev
* ``--certname`` - The certname that should be written to ``/etc/puppet/puppet.conf``. Defaults to client.grahamgilbert.dev
* ``--serial`` - The certname that will be written to``/etc/puppet/puppet.conf`` is set to the Mac's serial number.
* ``--clean_serial`` - The certname that will be written to``/etc/puppet/puppet.conf`` is set to the Mac's serial number, but with ``aaa`` prepended to it if the serial number starts with a number.
* ``--appendhosts`` - If you are using [vagrant-puppetmaster](https://github.com/grahamgilbert/vagrant-puppetmaster), this will append the default information into the client's ``/etc/hosts`` file so it can resolve the server.

## Example

``` bash
sudo python install_puppet.py --server puppet.example.com --certname my-client.example.com
```

Will install Puppet, write ``/etc/puppet/puppet.conf`` but will leave ``/etc/hosts`` untouched.

``` bash
sudo python install_puppet.py --appendhosts
```

Will produce a setup suitable for using with the defaults for [vagrant-puppetmaster](https://github.com/grahamgilbert/vagrant-puppetmaster).