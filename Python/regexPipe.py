#Regular expression PIPE

import re

heroRegEx = re.compile(r'batman|superman')

mo1 = heroRegEx.search('batman and superman')
print (mo1.group())

mo1 = heroRegEx.search('superman and batman')
print (mo1.group())
