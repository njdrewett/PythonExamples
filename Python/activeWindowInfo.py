#!python3

# Get active window info

import pyautogui

activeWindow = pyautogui.getActiveWindow()

print(str(activeWindow))

print(activeWindow.title)
print(activeWindow.size)
#resize window
activeWindow.width =1000

#move the active window
activeWindow.topleft = (800,400)



