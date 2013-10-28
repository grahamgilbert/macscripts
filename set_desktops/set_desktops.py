#!/usr/bin/python
 
'''Uses Cocoa classes via PyObjC to set a desktop picture on all screens.
Tested on Mountain Lion and Mavericks. Inspired by Greg Neagle's work: https://gist.github.com/gregneagle/6957826
 
See:
https://developer.apple.com/library/mac/documentation/cocoa/reference/applicationkit/classes/NSWorkspace_Class/Reference/Reference.html
 
https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html
 
https://developer.apple.com/library/mac/documentation/cocoa/reference/applicationkit/classes/NSScreen_Class/Reference/Reference.html
'''
 
from AppKit import NSWorkspace, NSScreen
from Foundation import NSURL
import argparse
import sys

parser = argparse.ArgumentParser(description='Sets the desktop picture on all screens')
parser.add_argument('--path', help='The path of the image')
args = vars(parser.parse_args())
 
if args['path']:
    picture_path = args['path']
else:
    print >> sys.stderr, 'You must supply a path for the desktop picture'
    exit(-1)
 
# generate a fileURL for the desktop picture
file_url = NSURL.fileURLWithPath_(picture_path)
 
# make image options dictionary
# we just make an empty one because the defaults are fine
options = {}
 
# get shared workspace
ws = NSWorkspace.sharedWorkspace()
 
# iterate over all screens
for screen in NSScreen.screens():
    # tell the workspace to set the desktop picture
    (result, error) = ws.setDesktopImageURL_forScreen_options_error_(
                file_url, screen, options, None)
    if error:
        print error
        exit(-1)