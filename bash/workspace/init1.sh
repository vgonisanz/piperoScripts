#!/bin/bash
sleep 1

# nice -10, launch process with priority: 10.
# nice --10, high priority: -10
# Priority is greater with lesser value.
# Negative nice value will increase the priority a the process.

# First: open apps
zenity --notification --text="Opening initial apps..."
nice -5 guake &
nice -10 ~/Programs/Telegram/Telegram -- %u &
nice -20 thunderbird &
nice -10 firefox &
nice -10 skype &
nice -10 nemo &
nice -9 atom &
# Wait enought time to load all apps
zenity --notification --text="Waiting until open..."
sleep 65

# Second: Move apps (r) to workspaces (t)
zenity --notification --text="Assigning workspaces..."
wmctrl -r ~/Programs/Telegram/Telegram -t 0
wmctrl -r skype -t 0
wmctrl -r thunderbird -t 1
wmctrl -r firefox -t 2
wmctrl -r atom -t 4 # text editor
wmctrl -r Home -t 4 # nemo folder window
sleep 1

# Third: Focus on firefox
zenity --info --text="Start to work!"
wmctrl -a firefox
