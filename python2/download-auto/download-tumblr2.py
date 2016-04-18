import argparse
import hashlib
import imghdr
import os, sys
from shutil import copyfileobj
from urllib import urlopen
from xml.etree import ElementTree as ET

def calculate_hash( file_name ):
   "Calculate Hash from a file"
   print "Calculating hash..."
   file_data = open(file_name).read()
   return hashlib.md5(file_data).hexdigest()

parser = argparse.ArgumentParser(description="Download all photos from your favorite tumblr. In example, to download from: http://tlkslksunited.tumblr.com/ use: python download-tumblr.py tlkslksunited")

# Required name tumblr
parser.add_argument('-n', action='store', dest='tumblr_name',
                    type=str, required=True,
                    help='The name of the tumblr target')

# Optional, output name a hash
parser.add_argument('--hash', action='store_true', dest='hash',
                    required=False,
                    help='Output name will be the photos HASHES')
# Try to parse the arguments
try:
    args = parser.parse_args()
except IOError, msg:
    parser.error(str(msg))
# All API info from tumblr at: https://www.tumblr.com/docs/en/api/v2
api_endpoint = 'http://%s.tumblr.com/api/read' % args.tumblr_name
start = 0
num = 50
post_count = 1
output_folder = args.tumblr_name
print "You have chosen tumblr: %s" % args.tumblr_name
if not os.path.exists(args.tumblr_name):
    print "Creating output folder"
    os.mkdir(args.tumblr_name)
else:
    print "Output folder already created!"
print "Downloading...."
while post_count:
    resp = urlopen("%s?type=photo&start=%s&num=%s" % (api_endpoint, start, num))
    content = resp.read()
    tree = ET.fromstring(content)
    post_tags = tree.findall(".//post")
    post_count = len(post_tags)
    for post_tag in post_tags:
        # Create name
        post_id = post_tag.attrib['id']
        post_date = post_tag.attrib['date-gmt'].split(" ")[0]
        outname = "%s-%s-%s" % (args.tumblr_name, post_date, post_id)
        photos_in_post = 0
        if os.path.exists(outname):
            print "%s already downloaded" % outname
            continue
        for photo_tag in post_tag.findall(".//photo-url"):
            # Download only bigger version
            if photo_tag.attrib['max-width'] == "1280":
                photo_url = photo_tag.text
                resp = urlopen(photo_url)
                outnamei = output_folder + '/' + outname + '_' + str(photos_in_post)
                outfile = open(outnamei, 'w')
                copyfileobj(resp, outfile)
                outfile.close()
                typefile = imghdr.what(outnamei)
                # Check if exist type
                if typefile == None:
                    print "Skipping NoneType..."
                    continue
                else:
                    typefile = "." + typefile
                photos_in_post += 1
                if args.hash:
                    hash_name = calculate_hash(outnamei)
                    hash_name = output_folder + '/' + hash_name + typefile
                    os.rename(outnamei, hash_name)
                    print "Downloaded photo with id %s posted at %s as %s" % (post_id, post_date, hash_name)
                else:
                    final_name = outnamei + typefile
                    os.rename(outnamei, final_name)
                    print "Downloaded photo with id %s posted at %s as %s" % (post_id, post_date, final_name)
    start += num
print "Download completed from $s" % args.tumblr_name
