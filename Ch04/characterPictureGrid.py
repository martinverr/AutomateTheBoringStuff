# automatetheboringstuff ch4: Character Picture Grid
# Note: The book suppose that the grid passed is valid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for y in range(len(grid[0])):   #y: 0 -> cols
    for x in range(len(grid)):  #x: 0 -> rows
        print(grid[x][y], end="")
    print()
