import imghdr
import glob, os
import argparse
import hashlib

def calculate_hash( file_name ):
   "Calculate Hash from a file"
   file_data = open(file_name).read()
   return hashlib.md5(file_data).hexdigest()

parser = argparse.ArgumentParser(description="Convert all file name in hist hash")

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
    file_path = os.path.dirname(os.path.abspath(file))
    typefile = imghdr.what(file)
    # Check if exist type
    if typefile == None:
        print "Skipping NoneType..."
        continue
    else:
        typefile = "." + typefile
    hash_name = calculate_hash(file)
    hash_name = file_path + '/' + hash_name + typefile
    print "Renaming from: " + file + " to: " + os.path.basename(hash_name)
    os.rename(file, hash_name)

print "done!"
