#! python3

#web browsing

# Using google maps via python using an address e.g. 1 Leighton Road Leighton Buzzard

import webbrowser
import sys
import pyperclip


#Read the command line arguments from sys.argv.

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    print("Address from command line: " + address)
#2. Read the clipboard contents.
else:
    # address from clipboard
    address = pyperclip.paste()
    print("Address from clipboard: " + address)

webbrowser.open('https://www.google.com/maps/place/' + address)



#3. Call the webbrowser.open() function to open the web browser.
