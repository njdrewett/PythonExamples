#! python3

import threading
import time

print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')
#end takeANap

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')

