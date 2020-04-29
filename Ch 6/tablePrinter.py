#Table Printer CH6

def printTable(toOrder):
    cols=len(toOrder[0])
    rows = len(toOrder)
    lenEachCol=[]
    maxTemp = 0
    
    for c in range(cols):
        for r in range(rows):
            if len(toOrder[r][c])>maxTemp:
                   maxTemp=len(toOrder[r][c])
        lenEachCol.append(maxTemp)
        maxTemp=0

    for r in range(rows):
        for c in range(cols):
            print(toOrder[r][c].ljust(lenEachCol[c]+1), end="")
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
