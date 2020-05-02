# AutomateTheBoringStuff Ch6: Table Printer
"""
Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
"""
def printTable(toOrder):
    cols=len(toOrder[0])
    rows = len(toOrder)
    lenEachCol=[]
    maxTemp = 0

    # get lenght of the longest word in each column
    for c in range(cols):
        for r in range(rows):
            if len(toOrder[r][c])>maxTemp:
                   maxTemp=len(toOrder[r][c])
        lenEachCol.append(maxTemp)
        maxTemp=0

    # print
    for r in range(rows):
        for c in range(cols):
            print(toOrder[r][c].ljust(lenEachCol[c]+1), end="")
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
