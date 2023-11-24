#Magic Eight Ball

import random

def buildAnswer(number):
    if number == 1:
        return 'it is certain'
    if number == 2:
        return 'It is decidedly so'
    if number == 3:
        return 'Yes'
    if number == 4:
        return 'No'
    if number == 5:
        return 'Ask again later'
    if number == 6:
        return 'Concentrate and ask again'
    if number == 7:
        return 'My reply is No'
    if number == 8:
        return 'Outlook is not good'
    if number == 9:
        return 'Very doubtful'

request = random.randint(1,9)
answer = buildAnswer(request)

print('Answer: ' + answer)

spam = print('Hello')
None == spam

print("Hello", end='')
print(" World")

print('cats','dogs','mice', sep=',')

def divisionOf42(divis):
    try:
        return 42 / divis
    except ZeroDivisionError:
        print('Error: divided by zero')

divisionOf42(7)
divisionOf42(0)

