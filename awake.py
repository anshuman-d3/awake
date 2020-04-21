# Awake - A cli utility for keeping the system awake while you are away.
# created by Anshuman
# 21-APR-2020 04:23 AM

import time
import argparse
import pyautogui
from datetime import datetime

parser = argparse.ArgumentParser(description="Awake - A cli utility for keeping the system awake while you are away.")
parser.add_argument('-i', '--idle', type=int, default=7,
                    help="Duration to takeover mouse actions. in seconds.")
parser.add_argument('-x', '--xaxis', type=int, default=10,
                    help="The amount of pixes to be moved during the action in x-axis. in pixels.")
parser.add_argument('-y', '--yaxis', type=int, default=0,
                    help="The amount of pixes to be moved during the action in y-axis. in pixels.")

args = vars(parser.parse_args())

IDLE_DURATION = args['idle']
MOVEMENT_X = args['xaxis']
MOVEMENT_Y = args['yaxis']

print("For configuring command line arguments and help type awake.py -h or --help.")
print('Current setting is, \n Idle duration = %s seconds \n Movement X = %s pixels\n Movement Y = %s pixels'
      % (IDLE_DURATION, MOVEMENT_X, MOVEMENT_Y))


def mouse_mover():
    while True:
        initial_cursor_position = pyautogui.position()
        time.sleep(IDLE_DURATION)
        if initial_cursor_position == pyautogui.position():
            print("Forward movement made at " + str(datetime.now().time()))
            pyautogui.press('shift')
            pyautogui.move(MOVEMENT_X, MOVEMENT_Y)
            time.sleep(5)
            pyautogui.move(-MOVEMENT_X, -MOVEMENT_Y)
            print("Reverse movement made at " + str(datetime.now().time()))


mouse_mover()
