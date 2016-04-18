import imghdr
import glob, os
import argparse

parser = argparse.ArgumentParser(description="Convert all files in a folder to its proper format")

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
    filename, file_extension = os.path.splitext(file)
    typefile = imghdr.what(file)
    # Check if exist type
    if typefile == None:
        print "Skipping NoneType..."
        continue
    else:
        typefile = "." + typefile
    # Replace if is needed
    if file_extension != typefile:
        update_filename = filename + typefile
        os.rename(file, update_filename)
        print "Converting " + file + " into " + update_filename

print "done!"
