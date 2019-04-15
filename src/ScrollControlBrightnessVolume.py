#! /usr/bin/python3

from evdev import InputDevice, ecodes
import subprocess
import sys

# path to mouse event
mouseEvent = '/dev/input/event8'

# amount of mouse movement to exit program
thresholdDistant = 30

# a percentage change in volume
volumeStep = "5"

# default controlType changes brightness
controlType = "brightness"
if len(sys.argv) > 1 and sys.argv[1] == "volume":
    controlType = "volume"

# read event of mouse from syste,
dev = InputDevice(mouseEvent)

# total mouse movement distance
amountOfMovement = 0

# multimedia keys to change brightness
# 1st element to turn down, the other to turn up
keys = ["XF86MonBrightnessDown", "XF86MonBrightnessUp"]

def ChangeBrightness(scrollValue, keys):
    # get 1st element which decreases the brightness when scrollValue < 0 or vice versa
    key = keys[scrollValue > 0]

    # send key using xdotool
    subprocess.run(["xdotool", "key", key])

def ChangeVolume(scrollValue, volumeStep):
    # percentage will be positive if scrollValue positive or vice versa
    vary = ['-', '+']
    percentage = ''.join([volumeStep, "%", vary[scrollValue > 0]])

    # send command to adjust volume
    subprocess.run(["amixer", "-qD", "pulse", "sset", "Master", percentage])


# parse mouse events
for event in dev.read_loop():
    # process mouse movement events only
    if event.type == ecodes.EV_REL:
        # track for mouse movement to exit when it leaves the corner
        if event.code in (ecodes.ABS_X, ecodes.ABS_Y):
            amountOfMovement += abs(event.value)
            if amountOfMovement > thresholdDistant: exit(0)
        # track for mouse scroll to change brightness or volume
        elif event.code == ecodes.REL_WHEEL:
            if controlType == "brightness":
                ChangeBrightness(event.value, keys)
            else:
                ChangeVolume(event.value, volumeStep)
