#!/usr/local/munki/munki-python

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
parser.add_argument('--secondpath', help='The path of second image')
parser.add_argument('--thirdpath', help='The path of third image')
args = vars(parser.parse_args())

picture_paths = []

if args['path']:
    picture_paths.append(args['path'])
else:
    print >> sys.stderr, 'You must supply a path for the desktop picture'
    exit(-1)
if args['secondpath']:
    picture_paths.append(args['secondpath'])
if args['thirdpath']:
    picture_paths.append(args['thirdpath'])

# make image options dictionary
# we just make an empty one because the defaults are fine
options = {}

# get shared workspace
ws = NSWorkspace.sharedWorkspace()

# Initialize screen counter
screen_counter = 0

# iterate over all screens
while counter < len(NSScreen.screens()):
    if counter > len(picture_paths):
        picture_counter = 0
    else:
        picture_counter = screen_counter
    # generate a fileURL for the desktop picture
    file_url = NSURL.fileURLWithPath_(picture_paths[picture_counter])
    print(f"Setting screen {screen_counter} to {picture_paths[picture_counter]}")
    # tell the workspace to set the desktop picture
    (result, error) = ws.setDesktopImageURL_forScreen_options_error_(
                file_url, NSScreen.screens[screen_counter], options, None)
    if error:
        print error
        exit(-1)
    screen_counter += 1

