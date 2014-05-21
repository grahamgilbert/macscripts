#!/bin/sh

# You need to change these.

# The Domain we're supposed to be on
DOMAIN="ad.company.com"

# The version of the package (today's date if created using the usual Luggage Makefile)
PKG_VERSION="20140401"

# The identifier of the package
PKG_ID="com.grahamgilbert.ad-bind"

## STOP EDITING ##

# The version from dsconfigad
ACTUAL_DOMAIN=`/usr/sbin/dsconfigad -show | /usr/bin/grep -i "Active Directory Domain" | /usr/bin/sed -n 's/[^.]*= //p'`

# The version installed from pkgutil
VERSION_INSTALLED=`/usr/sbin/pkgutil --pkg-info ${PKG_ID} | /usr/bin/grep version | /usr/bin/sed 's/^[^:]*: //'`
if [ "$ACTUAL_DOMAIN" = "$DOMAIN" ]
    then
    # We're on the right domain, make sure we've got the right version of the package
    if [ "$VERSION_INSTALLED" = "$PKG_VERSION" ]
    then
        # Everything's ok, no need to install
        exit 1
    else
        # Package is out of date, need to install
        exit 0
    fi
else
    # Domain isn't being returned from dsconfigad, need to install
    exit 0
fi