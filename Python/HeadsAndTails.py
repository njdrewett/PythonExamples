# Heads and Tails


import random

def tossCoin():
    result = random.randint(0,1)
    if(result == 0):
        return 'H'
    return 'T'


def tossCoins( tosses):
    streaks = 0
    currentToss = 'N'
    streakCount = 0;
    limit = range(0,tosses,1)
    for i in limit:
        coin = tossCoin()
#        print('Coin value ' + coin)
        if(currentToss == 'N'):
            #initialise
#            print('Initialising')
            currentToss = coin
            streakCount += 1
        else:
            if(currentToss == coin):
#                print(' A match ')
                streakCount += 1
                if(streakCount == 6):
                    print('Hit a 6 streak')
                    streaks += 1
            else:
                streakCount = 1
                currentToss = coin
            #end else
        #endelse

 #       print('['+str (i)+'] Streaks: ' + str(streaks) + ' currentToss: ' + currentToss + ' StreakCount : ' + str(streakCount) )
    #end for
    return streaks


numberOfStreaks = 0
for experimentNumber in range(10000):
 # Code that creates a list of 100 'heads' or 'tails' values.
 # Code that checks if there is a streak of 6 heads or tails in a row.
    streaks = tossCoins(100)
    print('Number of streaks: ' + str(numberOfStreaks) + ':streaks: ' + str(streaks))
    numberOfStreaks += streaks

    print('Chance of streak: %s%%' % (numberOfStreaks / 10000))
