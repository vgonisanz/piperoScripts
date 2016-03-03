#!/bin/bash
sleep 1

# First: open apps
notify-send "Opening initial apps..."
guake &
~/Programs/Telegram/Telegram -- %u &
thunderbird &
firefox &
skype &
nemo &
# Wait enought time to load all apps
sleep 30

# Second: Move apps (r) to workspaces (t)
notify-send "Assigning workspaces"
wmctrl -r ~/Programs/Telegram/Telegram -t 0
wmctrl -r skype -t 0
wmctrl -r thunderbird -t 1
wmctrl -r firefox -t 2
wmctrl -r nemo -t 3
sleep 1

# Third: Focus on firefox
notify-send "Workspace ready!"
wmctrl -a firefox
