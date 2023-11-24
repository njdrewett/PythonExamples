#! python3
#Bullet point adderr.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

## separate lines and add stars
lines = text.split('\n') # slipt by new line character
for i in range(0,len(lines)):
    lines[i] = "*" + lines[i]

joinlines = '\n'.join(lines)
text = joinlines

pyperclip.copy(text)






