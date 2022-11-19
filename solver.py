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

    # Check 3x3 box
    x_2 = (x//3)*3
    y_2 = (y//3)*3

    for i in range(9) :
        for j in range(9) :
            if (grid[i][x_2] == n) :
                if (grid[y_2][j] == n) :
                    return False
    return True

for i in range(9) :
    print(grid[i])

print(isPossible(7, 7, 3))