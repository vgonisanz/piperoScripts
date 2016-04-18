import argparse
import os

parser = argparse.ArgumentParser(description="Copy all file names into a txt file")

# Required name tumblr
parser.add_argument('-i', action='store', dest='input_path',
                    type=str, required=True,
                    help='The folder to check')

# Try to parse the arguments
try:
    args = parser.parse_args()
except IOError, msg:
    parser.error(str(msg))

current_path = os.getcwd()
final_path = current_path + "/output.txt"

print "Trying to open path: " + args.input_path
os.chdir(args.input_path)


print "Printing into: " + final_path
with open(final_path, "w") as a:
    for path, subdirs, files in os.walk(args.input_path):
       for filename in subdirs:
         print "File " + filename + " found."
         a.write(str(filename) + os.linesep)
