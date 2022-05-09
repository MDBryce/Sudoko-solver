
'''Creating the code to define the max numbers in the array and defining the puzzle class and functaionlity '''
M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, rows, cols, nums):
    for x in range(9):
        if grid[rows][x] == nums:
            return False
             
    for x in range(9):
        if grid[x][cols] == nums:
            return False
 
 
    startRow = rows - rows % 3
    startCol = cols - cols % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == nums:
                return False
    return True
 '''defining the Sudoko grid functaionlity'''
def Sudoko(grid, rows, cols):
 
    if (rows == M - 1 and cols == M):
        return True
    if cols == M:
        rows += 1
        cols = 0
    if grid[rows][cols] > 0:
        return Sudoko(grid, rows, cols + 1)
    for nums in range(1, M + 1, 1): 
     
        if solve(grid, rows, cols, nums):
         
            grid[rows][cols] = nums
            if Sudoko(grid, rows, cols + 1):
                return True
        grid[rows][cols] = 0
    return False
 
''' 0 means the cells are empty '''
grid = [[0, 0, 0, 9, 0, 0, 7, 0, 0],
    [5, 0, 7, 0, 0, 0, 1, 3, 0],
    [6, 4, 0, 0, 0, 3, 0, 8, 0],
    [0, 0, 0, 0, 4, 7, 8, 0, 0],
    [1, 7, 0, 8, 9, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 1, 0, 0, 6, 0, 5],
    [7, 0, 8, 6, 3, 9, 2, 0, 4],
    [2, 6, 1, 0, 7, 5, 3, 0, 8]]
 
if (Sudoko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist")