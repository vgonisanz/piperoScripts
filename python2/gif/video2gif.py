import os
import sys
import argparse
from moviepy.editor import *

# variables
current_path = os.getcwd()
complete_output_filename = "./output/test.gif"
complete_input_filename = "./input/test.avi"
initial_min_time = 1
initial_sec_time = 21.00
final_min_time = 1
final_sec_time = 22.00
scale = 1.0
output_fps = 15
# crop
# <---out x1 | inside gif \ x2 out--->
cropx1 = 0
cropx2 = 9999
cropy1 = 0
cropy2 = 9999

# Functions
def print_variables():
    "This prints configuration variables"
    print "Processing: " + str(complete_input_filename)
    print "To create: " + str(complete_output_filename)
    print "From: " + str(initial_min_time) + "," + str(initial_sec_time) + \
    " to: " + str(final_min_time) + "," + str(final_sec_time)
    print "Scale original video x" + str(scale)
    print "With " + str(output_fps) + " frames per sec"
    #print "Duration is: " (final_time - initial_time)
    return


# Usage:
parser = argparse.ArgumentParser(description="Create your gif from a video \
Example: \
python video2gif.py -v -i \"/home/piperoman/work/git/piperoScripts/python2/gif/input/test.avi\" -startm 1 -starts 32.00 -endm 1 -ends 33.00 \
")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
#parser.add_argument("-f", type=str, help="Input file name")
parser.add_argument("-i", type=str, dest='complete_input_filename', help="Input file")
parser.add_argument("-o", type=str, dest='complete_output_filename', help="Output path for the gif")
parser.add_argument("-startm", type=int, dest='initial_min_time', help="Initial minute time of the gif")
parser.add_argument("-starts", type=float, dest='initial_sec_time', help="Initial second time of the gif")
parser.add_argument("-endm", type=int, dest='final_min_time', help="End minute time of the gif")
parser.add_argument("-ends", type=float, dest='final_sec_time', help="End second time of the gif")
parser.add_argument("-scale", type=float, dest='scale', help="Scale video size in the gif")
parser.add_argument("-fps", type=int, dest='output_fps', help="Final fps in the gif")
parser.add_argument("-cropx1", type=int, dest='cropx1', help="remove pixels from 0 to x1")
parser.add_argument("-cropx2", type=int, dest='cropx2', help="remove pixels from x2 to video width")
parser.add_argument("-cropy1", type=int, dest='cropy1', help="remove pixels from 0 to y1")
parser.add_argument("-cropy2", type=int, dest='cropy2', help="remove pixels from y2 to video height")

# Try to parse the arguments
try:
    args = parser.parse_args()
except IOError, msg:
    parser.error(str(msg))

# Calculate variables needed
if args.complete_input_filename is not None:
    complete_input_filename = args.complete_input_filename
if args.complete_output_filename is not None:
    complete_output_filename = args.complete_output_filename
if args.initial_min_time is not None:
    initial_min_time = args.initial_min_time
if args.initial_sec_time is not None:
    initial_sec_time = args.initial_sec_time
if args.final_min_time is not None:
    final_min_time = args.final_min_time
if args.final_sec_time is not None:
    final_sec_time = args.final_sec_time
if args.output_fps is not None:
    output_fps = args.output_fps
if args.scale is not None:
    scale = args.scale
if args.cropx1 is not None:
    cropx1 = args.cropx1
if args.cropx2 is not None:
    cropx2 = args.cropx2
if args.cropy1 is not None:
    cropy1 = args.cropy1
if args.cropy2 is not None:
    cropy2 = args.cropy2

if args.verbose:
    print_variables()

# Process
print "Processing..."
file_exist = os.path.isfile(complete_input_filename)
if not file_exist:
    print "File " + complete_input_filename + " no exist. Aborting..."
    sys.exit()

# Add hour to subclip?
clip = (VideoFileClip(complete_input_filename)
        .subclip((initial_min_time,initial_sec_time),(final_min_time,final_sec_time))
        .resize(scale)
        .crop(x1=cropx1, x2=cropx2, y1=cropy1, y2=cropy2)
        )

# Write final gif
#composition = CompositeVideoClip([clip])
#composition.write_gif('output/anna_olaf.gif', fps=15)

clip.write_gif(complete_output_filename, fps=output_fps)

# http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/

#kris_sven = (VideoFileClip("frozen_trailer.mp4")
#             .subclip((1,13.4),(1,13.9))
#             .resize(0.5)
#             .crop(x1=145,x2=400)) # remove left-right borders
#kris_sven.write_gif("kris_sven.gif")
#anna_olaf = (VideoFileClip("frozen_trailer.mp4")
#             .subclip(87.9,88.1)
#             .speedx(0.5) # Play at half speed
#             .resize(.4))

#snapshot = (anna_olaf
#            .crop(x2= anna_olaf.w/2) # remove right half
#            .to_ImageClip(0.2) # snapshot of the clip at t=0.2s
#            .set_duration(anna_olaf.duration))

#composition = CompositeVideoClip([anna_olaf, snapshot])
#composition.write_gif('anna_olaf.gif', fps=15)

#import moviepy.video.tools.drawing as dw

#anna_kris = (VideoFileClip("frozen_trailer.mp4", audio=False)
#             .subclip((1,38.15),(1,38.5))
#             .resize(.5))

# coordinates p1,p2 define the edges of the mask
#mask = dw.color_split(anna_kris.size, p1=(445, 20), p2=(345, 275),
#                      grad_width=5) # blur the mask's edges

#snapshot = (anna_kris.to_ImageClip()
#            .set_duration(anna_kris.duration)
#            .set_mask(ImageClip(mask, ismask=True))

#composition = CompositeVideoClip([anna_kris,snapshot]).speedx(0.2)
# 'fuzz' (0-100) below is for gif compression
#composition.write_gif('anna_kris.gif', fps=15, fuzz=3)

#def time_symetrize(clip):
#    """ Returns the clip played forwards then backwards. In case
#    you are wondering, vfx (short for Video FX) is loaded by
#    >>> from moviepy.editor import * """
#    return concatenate([clip, clip.fx( vfx.time_mirror )])

#clip = (VideoFileClip("frozen_trailer.mp4", audio=False)
#        .subclip(36.5,36.9)
#        .resize(0.5)
#        .crop(x1=189, x2=433)
#        .fx( time_symetrize ))

#clip.write_gif('sven.gif', fps=15, fuzz=2)

#olaf = (VideoFileClip("frozen_trailer.mp4", audio=False)
#        .subclip((1,21.6),(1,22.1))
#        .resize(.5)
#        .speedx(0.5)
#        .fx( time_symetrize ))

# Many options are available for the text (requires ImageMagick)
#text = (TextClip("In my nightmares\nI see rabbits.",
#                 fontsize=30, color='white',
#                 font='Amiri-Bold', interline=-25)
#        .set_pos((20,190))
#        .set_duration(olaf.duration))

#composition = CompositeVideoClip( [olaf, text] )
#composition.write_gif('olaf.gif', fps=10, fuzz=2)
