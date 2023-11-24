# Regular Expressions

import re

searchString = 'My phone number is: 123-123-1234'
unitedStatesPhoneNumberRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = unitedStatesPhoneNumberRegEx.search(searchString)
print('Phone number is: {}'.format(mo.group()) )

groupedPhoneNumberRegEx = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = groupedPhoneNumberRegEx.search(searchString)
print('Whole Phone number is: {}'.format(mo.group(0)) )
print('Phone number area code is: {}'.format(mo.group(1)) )
print('Phone number is: {}'.format(mo.group(2)) )
areaCode, mainNumber = mo.groups()
print(areaCode + ":" + mainNumber)
