grid = [[6, 0, 1, 0, 0, 0, 9, 0, 0],
        [0, 4, 0, 5, 7, 6, 0, 8, 0],
        [0, 0, 0, 4, 0, 0, 5, 6, 2],
        [8, 0, 2, 0, 0, 9, 0, 0, 3],
        [0, 3, 6, 0, 0, 0, 7, 1, 0],
        [9, 0, 0, 3, 0, 0, 8, 0, 5],
        [4, 6, 7, 0, 0, 3, 0, 0, 0],
        [0, 2, 0, 7, 1, 8, 0, 9, 0],
        [0, 0, 8, 0, 0, 0, 2, 0, 7]]

def isPossible(x, y, n) :
    # Check row
    for i in range(9) :
        if (grid[i][x] == n) :
            return False
    # Check column
    for j in range(9) :
        if (grid[y][j] == n) :
            return False
    return True

for i in range(9) :
    print(grid[i])

print(isPossible(0, 2, 7))