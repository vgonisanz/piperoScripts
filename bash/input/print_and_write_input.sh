#!/bin/sh
#
# run as root, use od and tee
#
echo "Reading input event 4"
OUTPUT=$(pwd)
OUTPUTFILE=${OUTPUT}/output.raw
echo "Output: ${OUTPUTFILE}"
od -x /dev/input/event4 | tee ${OUTPUTFILE}
