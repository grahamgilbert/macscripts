#!/bin/bash
file="/usr/sbin/jamf"
if [ -f "$file" ]
then
	exit 0
else
	exit 1
fi