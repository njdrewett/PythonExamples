# Character picture grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


height = len(grid)
print(str(height))
width = len(grid[0])
print(str(width))

# loop height before row
heightRange = range(0,height,1)
widthRange = range(0,width,1)

for i in widthRange:
    for k in heightRange:
        print(str(grid[k][i]), end='')
    print()



