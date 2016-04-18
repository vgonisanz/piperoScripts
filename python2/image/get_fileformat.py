import imghdr
import glob, os
import argparse

parser = argparse.ArgumentParser(description="Get the format of all files in a folder")

# Required name tumblr
parser.add_argument('-p', action='store', dest='input_path',
                    type=str, required=True,
                    help='The folder to check')

# Try to parse the arguments
try:
    args = parser.parse_args()
except IOError, msg:
    parser.error(str(msg))

print "Trying to open path: " + args.input_path
os.chdir(args.input_path)

print "Printing...."
for file in glob.glob("*.*"):
    typefile = imghdr.what(file)
    print "File: " + file + " is a " + typefile

print "done!"
