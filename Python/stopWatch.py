#!python3

# StopWatch Program

#1. Track the amount of time elapsed between presses of the enter key,
# with each key press starting a new “lap” on the timer.
#2. Print the lap number, total time, and lap time

import time

#1. Find the current time by calling time.time() and store it as a timestamp
#at the start of the program, as well as at the start of each lap.

currentTime = time.time()
# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started..')

startTime = time.time()
lastTime = startTime
lapNumber = 1

try :
#2. Keep a lap counter and increment it every time the user presses enter.
    while True:
        input()

    #3. Calculate the elapsed time by subtracting timestamps.
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print("Lap %s , Lap time: %s  , Total Time: %s" % (lapNumber, lapTime, totalTime))
        lapNumber += 1
        lastTime = time.time()
#4. Handle the KeyboardInterrupt exception so the user can press ctrl-C
#to quit
except KeyboardInterrupt:
    # Handling keyboard ctrl-C
    print("Done..")


