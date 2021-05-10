#Importing the Libraries
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# Click function to click the block on possible location
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Exit when "q" is Pressed
while keyboard.is_pressed('q') == False:
    
    # Location of Block tiles
    # i,e, 
    # 1st Block
    if pyautogui.pixel(750,653)[0] == 0:
        click(750,653)
    # 2nd Block
    if pyautogui.pixel(895,653)[0] == 0:
        click(895,653)
    # 3rd Block
    if pyautogui.pixel(1030,653)[0] == 0:
        click(1030,653)
    # 4th Block
    if pyautogui.pixel(1155,653)[0] == 0:
        click(1155,653)