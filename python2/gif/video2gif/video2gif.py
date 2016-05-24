import os
import sys
import argparse
from moviepy.editor import *

############
# variables
############
current_path = os.getcwd()
complete_output_filename = "./output/test.gif"
complete_input_filename = "./input/test.avi"
initial_hour_time = 0
initial_min_time = 0
initial_sec_time = 0.00
final_hour_time = 0
final_min_time = 0
final_sec_time = 1.00
scale = 1.0
output_fps = 12
speedx = 1.0
# Margin remove (0, marginx1 | data | marginx2, width)
marginx1 = 0
marginx2 = 0
marginy1 = 0
marginy2 = 0
# text variables
text_value = " "
text_fontsize = 30
text_color='white'
text_font='Amiri-Bold'
text_interline=-25
text_position_x = 20
text_position_y = 190
text_duration = -1  # If -1 use clip duration

############
# Functions
############
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

def processvideo2gif(   complete_input_filename, complete_output_filename,
                        initial_hour_time, initial_min_time, initial_sec_time, final_hour_time, final_min_time, final_sec_time,
                        scale, speedx, marginx1, marginx2, marginy1, marginy2, output_fps,
                        text_value, text_fontsize, text_color, text_font, text_interline, text_position_x, text_position_y, text_duration):

    videowidth = VideoFileClip(complete_input_filename).w
    videoheight = VideoFileClip(complete_input_filename).h
    print "Processing video with size " + str(videowidth) + "x" + str(videoheight)

    # Assing crop parameters to remove margin only
    cropx1 = marginx1
    cropx2 = videowidth - marginx2
    cropy1 = marginy1
    cropy2 = videoheight - marginy2

    # Add hour to subclip?
    clip = (VideoFileClip(complete_input_filename)
            .subclip((initial_hour_time, initial_min_time,initial_sec_time),(final_hour_time, final_min_time,final_sec_time))
            .resize(scale)
            .crop(x1=cropx1, x2=cropx2, y1=cropy1, y2=cropy2)
            .speedx(speedx)
            )

    # Add text if needed
    if text_duration == -1:
        text_duration = clip.duration

    text = (TextClip(text_value, fontsize=text_fontsize, color=text_color, font=text_font, interline=text_interline)
            .set_pos((text_position_x,text_position_y))
            .set_duration(text_duration))

    composition = CompositeVideoClip( [clip, text] )

    # Write final gif
    composition.write_gif(complete_output_filename, fps=output_fps, fuzz=2)
    return

# Usage:
parser = argparse.ArgumentParser(description="Create your gif from a video \
Example: \
python video2gif.py -v -i \"./input/test.avi\" -startm 1 -starts 1.00 -endm 1 -ends 2.00 \
")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
# file
parser.add_argument("-i", type=str, dest='complete_input_filename', help="Input file")
parser.add_argument("-o", type=str, dest='complete_output_filename', help="Output path for the gif")
# time
parser.add_argument("-starth", type=int, dest='initial_hour_time', help="Initial hour time of the gif")
parser.add_argument("-startm", type=int, dest='initial_min_time', help="Initial minute time of the gif")
parser.add_argument("-starts", type=float, dest='initial_sec_time', help="Initial second time of the gif")
parser.add_argument("-endh", type=int, dest='final_hour_time', help="End hour time of the gif")
parser.add_argument("-endm", type=int, dest='final_min_time', help="End minute time of the gif")
parser.add_argument("-ends", type=float, dest='final_sec_time', help="End second time of the gif")
# parameters
parser.add_argument("-scale", type=float, dest='scale', help="Scale video size in the gif")
parser.add_argument("-speedx", type=float, dest='speedx', help="Speed factor in the gif")
parser.add_argument("-fps", type=int, dest='output_fps', help="Final fps in the gif")
# crop
parser.add_argument("-marginx1", type=int, dest='marginx1', help="remove pixels from 0 to x1")
parser.add_argument("-marginx2", type=int, dest='marginx2', help="remove pixels from x2 to video width")
parser.add_argument("-marginy1", type=int, dest='marginy1', help="remove pixels from 0 to y1")
parser.add_argument("-marginy2", type=int, dest='marginy2', help="remove pixels from y2 to video height")
# text
parser.add_argument("-text_value", type=str, dest='text_value', help="Text value")
parser.add_argument("-text_fontsize", type=int, dest='text_fontsize', help="Text fontsize")
parser.add_argument("-text_color", type=str, dest='text_color', help="Text color")
parser.add_argument("-text_font", type=int, dest='text_font', help="Text font")
parser.add_argument("-text_interline", type=int, dest='text_interline', help="Text interline")
parser.add_argument("-text_position_x", type=int, dest='text_position_x', help="Position X to the text")
parser.add_argument("-text_position_y", type=int, dest='text_position_y', help="Position Y to the text")
parser.add_argument("-text_duration", type=float, dest='text_duration', help="Duration of the text, -1 = clip duration")

# Try to parse the arguments
try:
    args = parser.parse_args()
except IOError, msg:
    parser.error(str(msg))

# Parse arguments if exist
# files
if args.complete_input_filename is not None:
    complete_input_filename = args.complete_input_filename
if args.complete_output_filename is not None:
    complete_output_filename = args.complete_output_filename
# time
if args.initial_hour_time is not None:
    initial_hour_time = args.initial_hour_time
if args.initial_min_time is not None:
    initial_min_time = args.initial_min_time
if args.initial_sec_time is not None:
    initial_sec_time = args.initial_sec_time
if args.final_hour_time is not None:
    final_hour_time = args.final_hour_time
if args.final_min_time is not None:
    final_min_time = args.final_min_time
if args.final_sec_time is not None:
    final_sec_time = args.final_sec_time
# parameters
if args.output_fps is not None:
    output_fps = args.output_fps
if args.scale is not None:
    scale = args.scale
if args.speedx is not None:
    speedx = args.speedx
# crop
if args.marginx1 is not None:
    marginx1 = args.marginx1
if args.marginx2 is not None:
    marginx2 = args.marginx2
if args.marginy1 is not None:
    marginy1 = args.marginy1
if args.marginy2 is not None:
    marginy2 = args.marginy2
# text
if args.text_value is not None:
    text_value = args.text_value
if args.text_fontsize is not None:
    text_fontsize = args.text_fontsize
if args.text_color is not None:
    text_color = args.text_color
if args.text_font is not None:
    text_font = args.text_font
if args.text_interline is not None:
    text_interline = args.text_interline
if args.text_position_x is not None:
    text_position_x = args.text_position_x
if args.text_position_y is not None:
    text_position_y = args.text_position_y
if args.text_duration is not None:
    text_duration = args.text_duration

# Verbose option
if args.verbose:
    print_variables()

# Process
print "Processing..."
file_exist = os.path.isfile(complete_input_filename)
if not file_exist:
    print "File " + complete_input_filename + " no exist. Aborting..."
    sys.exit()

processvideo2gif(       complete_input_filename, complete_output_filename,
                        initial_hour_time, initial_min_time, initial_sec_time, final_hour_time, final_min_time, final_sec_time,
                        scale, speedx, marginx1, marginx2, marginy1, marginy2, output_fps,
                        text_value, text_fontsize, text_color, text_font, text_interline, text_position_x, text_position_y, text_duration
                        )

# http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/
