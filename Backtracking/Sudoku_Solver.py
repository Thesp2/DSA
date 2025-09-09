def isvalid(grid,r,c,num):
    if num in grid[r]:
        return False
    for i in range(9):
        if grid[i][c]==num:
            return False
        
    startr,startc=(r//3)*3,(c//3)*3
    for i in range(startr,startr+3):
        for j in range(startc,startc+3):
            if grid[i][j]==num:
                return False
    return True

def solve(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c]==0:
                for num in range(1,10):
                    if isvalid(grid,r,c,num):
                        grid[r][c]=num
                        if solve(grid):
                            return True
                        grid[r][c]=0
                return False
    return True

def print_sudoku(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:   
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:  
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()

sudoku = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

print("Initial Sudoku:")
print_sudoku(sudoku)

solve(sudoku)

print("\nSolved Sudoku:")
print_sudoku(sudoku)
