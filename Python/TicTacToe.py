# Tic tac toe

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard():
    print(theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
    print('-+-+-')
    print(theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print('-+-+-')
    print(theBoard['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R'])

printBoard()

turn = 'X'

for i in range(9):
    printBoard()
    print('Turn for ' + turn + '. What is your input?')
    space = input()
    theBoard[space] = turn
    if(turn == 'X'):
        turn = 'O'
    else:
        turn = 'X'



