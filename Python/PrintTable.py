#print table

tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

def longestWordLength(items):
    longest = 0
    for word in items:
        currentLength = len(word)
    #print('currentLength: ' + str(currentLength))
        if( currentLength > longest):
            longest = currentLength
        #endif
    #endfor
#    print('Longest length: ' + str(longest))

    return longest
#enddef

def printTable(items):
    # find longest word in list
    longestLength = []
    index = 0
    for itemList in items:
        longest = longestWordLength(itemList)
        longestLength.append(longest)
    #endfor
    maxColumns = len(items)
    maxRows = len(items[0])
    for row in range(0,maxRows):
        for column in range(0,maxColumns):
            print(items[column][row].rjust(longestLength[column],' ') ,end =' ')
        #endfor
        print()
    #endfor
#enddef

printTable(tableData)
