#! /usr/bin/python3

from evdev import InputDevice, ecodes
import subprocess

# read event of mouse from syste,
dev = InputDevice('/dev/input/event8')

# amount of mouse movement to exit program
thresholdDistant = 30

# total mouse movement distance
amountOfMovement = 0

def ChangeBrightness(scrollValue):
    # update brightness of screen
    
    key = "XF86MonBrightnessUp"
    if scrollValue < 0:
        key = "XF86MonBrightnessDown"

    # send key using xdotool
    subprocess.run(["xdotool", "key", key])


# parse mouse events
for event in dev.read_loop():
    # process mouse movement events only
    if event.type == ecodes.EV_REL:
        # track for mouse movement to exit when it leaves the corner
        if event.code in (ecodes.ABS_X, ecodes.ABS_Y):
            amountOfMovement += abs(event.value)
            if amountOfMovement > thresholdDistant: exit(0)
        # track for mouse scroll to change brightness
        elif event.code == ecodes.REL_WHEEL:
            ChangeBrightness(event.value)