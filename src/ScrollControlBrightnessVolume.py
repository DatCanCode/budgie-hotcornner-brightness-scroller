#! /usr/bin/python3

from evdev import InputDevice, ecodes
import subprocess
import sys

# path to mouse event
mouseEvent = '/dev/input/event8'

# amount of mouse movement to exit program
thresholdDistant = 30

# default keytype changes brightness
keytype = "brightness"
if len(sys.argv) > 1 and sys.argv[1] == "volume":
    keytype = "volume"

# read event of mouse from syste,
dev = InputDevice(mouseEvent)

# total mouse movement distance
amountOfMovement = 0

# multimedia keys for change volume and brightness
# each type has a set. 1st element to turn down, the other to turn up
keys = {
    "brightness": ["XF86MonBrightnessDown", "XF86MonBrightnessUp"],
    "volume": ["XF86AudioLowerVolume", "XF86AudioRaiseVolume"]
}

def ChangeBrightnessVolume(scrollValue, keys, keytype):
    # update brightness and volume
    
    key = keys[keytype][scrollValue > 0]

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
        # track for mouse scroll to change brightness or volume
        elif event.code == ecodes.REL_WHEEL:
            ChangeBrightnessVolume(event.value, keys, keytype)