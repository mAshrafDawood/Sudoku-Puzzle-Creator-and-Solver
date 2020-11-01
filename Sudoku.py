import numpy as np
import requests


print("Welcome to Soduko puzzle creator & solver")
print("Level 1 (Hardest with usually 1 solution)\nlevel 2 (Intermediate with usually couple of solutions)\nLevel 3 (Easiest with multiple solutions3)")
lvl = int(input("Level --> "))
url = "http://www.cs.utep.edu/cheon/ws/sudoku/new/"
headers = {
    "size":9,
    "level":lvl
}

r = requests.get(url, params=headers)
grid_fills = r.json()["squares"]

#Creating empty grid
grid = []
for i in range(9):
    grid.append([])
    for j in range(9):
        grid[i].append(0)

#Filling spaces
for i in range(9):
    for j in range(9):
        for grid_fill in grid_fills:
            if grid_fill['x'] == i and grid_fill['y'] == j:
                grid[i][j] = grid_fill['value']
            
print(np.matrix(grid))


def possible(y, x, n):
    global grid
    for i in range(9):
        if n == grid[y][i]:
            return False
    for i in range(9):
        if n == grid[i][x]:
            return False
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if n == grid[y0+i][x0+j]:
                return False
    return True


def Solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        Solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    z = input("Attempt to find another solution ? (y/n)").strip().lower()
    assert z == 'y' or z == 'n';
    if z == 'n':
        return
        
    


z = input("Solve ? (y/n)").strip().lower()
assert z == 'y' or z=='n'
if z == 'y':
    Solve()
    print("No more solutions found. Press Enter to exit")
    input()
else:
    print("Press enter to close ...")
    input()

