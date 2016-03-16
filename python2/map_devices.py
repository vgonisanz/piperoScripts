#!/usr/bin/env python2
# script for printing device information of /dev/input/event* devices
#

import os
import sys
import evdev as ev

def checkRoot():
	if os.getuid()!=0:
		print '[*] You need root for that'
		return False
	return True

if not checkRoot():
	sys.exit(1)

devList = ev.list_devices()
devList.reverse()
for inp in devList:
	dev = ev.InputDevice(inp)
	print "-"*60
	print "[%s]" % inp
	print "%s\n%s\n%s" % (dev.name, dev.info,dev.phys)
print "-"*60
