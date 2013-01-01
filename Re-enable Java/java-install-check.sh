#!/bin/bash


javaVendor=`/usr/bin/defaults read /Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Info CFBundleIdentifier`

 

if [ "$javaVendor" = "com.oracle.java.JavaAppletPlugin" ]; then

        result=Oracle
		exit 0

elif [ "$javaVendor" = "com.apple.java.JavaAppletPlugin" ]; then

        result=Apple
		exit 1
elif [ "$javaVendor" = "com.apple.java.JavaPlugin2_NPAPI"]; then
    result=Symlinked
    exit 1

elif [ "$javaVendor" = "" ]; then

        result="No Java Plug-In Available"
		exit 1

fi

 