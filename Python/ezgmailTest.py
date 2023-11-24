#!python3e your code here :-)
import ezgmail
import os


ezgmail.init()

#ezgmail.send('njdrewett@sky.com', 'Test Subject line', 'Test Body of the email')
unreadThreads = ezgmail.unread() # List of GmailThread objects.

ezgmail.summary(unreadThreads)
