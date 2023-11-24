#Conways Game of Life

import random, time, copy

WIDTH=60
HEIGHT = 20

nextCells = []
for x in range(WIDTH):
    column = [] # create new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')
        else :
            column.append(' ')
    nextCells.append(column)

while True:
    print('\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    # print current cells on screensize
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()
    # calculate the next steps cells based on the current steps cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get neighbouring coordinates
            # `%WIDTH` ensures leftCoord is always between 0 and width -1
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            numNeighbours = 0
            # Count number of living neighbours
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbours += 1 # topleft is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbours += 1 # top is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbours += 1 # top is alive

            # Count number of living neighbours
            if currentCells[leftCoord][y] == '#':
                numNeighbours += 1 # topleft is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbours += 1 # top is alive

           # Count number of living neighbours
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbours += 1 # belowCoord is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbours += 1 # belowCoord is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbours += 1 # belowCoord is alive

            # Set cell based on Conways Game Of Life Rules:
            if currentCells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
                # living cells with 2 or 3 neighbours stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbours == 3:
                # Dead cells become alive
                nextCells[x][y] = '#'
            else :
                # everything else dies
                nextCells[x][y] = ' '
    time.sleep(0.5)



