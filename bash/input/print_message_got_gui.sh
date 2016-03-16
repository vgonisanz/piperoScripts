#!/bin/sh
#
# run, ask for a message, and print
# 
echo "Asking for a message"
my_message=$(zenity --entry --title="Hi user" --text="Enter a message:")
zenity --info --text="Your message: ${my_message}"
