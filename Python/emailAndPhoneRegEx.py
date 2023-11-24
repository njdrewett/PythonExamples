# Phone number and email address extractor

import pyperclip
import re

phoneNumberRegEx = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 (\d{3}) # first 3 digits
 (\s|-|\.) # separator
 (\d{4}) # last 4 digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
 )''', re.VERBOSE)

emailRegex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+ # username
  @ # @ symbol
  [a-zA-Z0-9.-]+ # domain name
 (\.[a-zA-Z]{2,4}) # dot-something
 )''', re.VERBOSE)


## Pull text off of clipboard
def pullClipboardText():
    text = pyperclip.paste()
    return text
#enddef

text = pullClipboardText()
# Find all phone numbers and email addresses from text
phoneNumbers  = phoneNumberRegEx.findall(text)
emailAddresses = emailRegex.findall(text)

for group in phoneNumbers :
    print(group)

for group in emailAddresses:
        print(group)


# paste them into clipboard.


