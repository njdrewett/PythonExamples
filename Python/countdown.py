#! python3

#Countdown example using threads

# 1. Count down from 60.
# 2. Play a sound file (alarm.wav) when the countdown reaches zero

import time
import subprocess


timeLeft = 6
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['start', 'alarm.wav'], shell=True)


