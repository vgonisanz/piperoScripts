# Description: http://pyautogui.readthedocs.io/en/latest/cheatsheet.html

import time
import notify2
import _thread
import sys, os
import argparse
import tkinter
import pyautogui
import pyglet

# Variable definition
global app_name
global screenOffset   # Avoid problem with corner
global screenWidth
global screenHeight
app_name = "Input python3 Tutorial"
screenOffset = 1
screenWidth = 0
screenHeight = 0

# Function definition
def initialize():
    # Initialize notifications
    notify2.init(app_name)
    #notify2.Notification(app_name, 'Initializing...').show()

    # Initialize GUI
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True

    # Screen size
    # (0,0) ---> X ++
    # |
    # |
    # v
    # Y ++
    global screenWidth, screenHeight
    screenWidth, screenHeight = pyautogui.size()
    print("Resolution: " + str(screenWidth) + "x" + str(screenHeight))

def moveMouseAbsoluteSample():
    print("Testing absolute mouse positions")

    # Move absolute positions
    pyautogui.moveTo(screenOffset, screenOffset, duration=0.25)
    pyautogui.moveTo(screenWidth, screenOffset, duration=0.25)
    pyautogui.moveTo(screenWidth, screenHeight, duration=0.25)
    pyautogui.moveTo(screenOffset, screenHeight, duration=0.25)

def moveMouseRelativeSample():
    print("Testing relative to (100,100) mouse positions")

    # Init position (100x100)
    pyautogui.moveTo(100, 100, duration=0.25)

    # Move relative
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)

def temp():
    pyautogui.alert('This displays some text with an OK button.')
    pyautogui.position()  # current mouse x and y
    pyautogui.onScreen(x, y)  # True if x & y are within the screen.
    pyautogui.PAUSE = 2.5   # Pause 2.5 s
    pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
    pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  # drag mouse relative to its current position
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left') # The button keyword argument can be 'left', 'middle', or 'right'.
    pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
    pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
    pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')
    pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)  # useful for entering text, newline is Enter
    pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)
    pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
    pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste
    pyautogui.alert('This displays some text with an OK button.')
    pyautogui.confirm('This displays text and has an OK and Cancel button.')
    pyautogui.prompt('This lets the user type in a string and press OK.')
    pyautogui.screenshot('foo.png')  # returns a Pillow/PIL Image object, and saves it to a file
    pyautogui.locateOnScreen('looksLikeThis.png')
    pyautogui.locateCenterOnScreen('looksLikeThis.png')  # returns center x and y



def do_all():
    print("All")
    moveMouseAbsoluteSample()
    moveMouseRelativeSample()

def do_current():
    #moveMouseAbsoluteSample()
    print("Current")
    #window = pyglet.window.Window()
    #image = pyglet.image.load('cursor_win_crosshair.png')
    #cursor = pyglet.window.ImageMouseCursor(image, 16, 8)
    #window.set_mouse_cursor(cursor)
    time.sleep(5)

def do_test():
    tkinter._test()

def check_args():
    usage = "usage: %prog [options]"
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--all", action="store_true", dest="do_all", default=False, help="Do all input procedures")
    parser.add_argument("-c", "--current", action="store_true", dest="do_current", default=False, help="Just testing current feature (Temporal)")
    parser.add_argument("-t", "--test", action="store_true", dest="do_test", default=False, help="Just testing dependencies")
    args = parser.parse_args()

    if (args.do_all==False and args.do_test==False and args.do_current==False): # No option
        parser.print_help()
        sys.exit(0)
    if (args.do_all==True):
        do_all()
    if (args.do_current==True):
        do_current()
    if (args.do_test==True):
        do_test()

if __name__ == '__main__':
    print("Introduction to input scripts with python3")


    initialize()
    check_args()
    print("done.")
    #threading.main_thread()
