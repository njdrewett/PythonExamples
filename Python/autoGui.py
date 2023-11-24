#! python3

# Automated GUI

import pyautogui

widthHeight = pyautogui.size()
print(widthHeight)

for i in range(5):
    pyautogui.moveTo(100,100,duration=0.25)
    pyautogui.moveTo(200,100,duration=0.25)
    pyautogui.moveTo(200,200,duration=0.25)
    pyautogui.moveTo(100,200,duration=0.25)

pyautogui.click(10, 5)
