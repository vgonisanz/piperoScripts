#!/bin/sh
#
# run as root, uses dumpkeys
#
echo "If run as root, print dictionary with keyboard maps"
echo "myDict={\\"
dumpkeys |grep "^keycode"|sed -e 's/  / /g'|sed -e 's/  / /g'|cut -d ' ' -f 2,4|sed 's/ /:\"/g'|sed -e 's/$/\",/g'|tr -d '\n'
echo "}"
