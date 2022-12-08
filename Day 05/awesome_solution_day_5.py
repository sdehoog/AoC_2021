import numpy as np

grid = np.zeros((2, 1000, 1000))
ls = np.fromregex(open('input.txt'), '\d+', [('',int)]*4)

for (x, y, X, Y) in ls:
    dx, dy = np.sign([X-x, Y-y])                 
    while (x,y) != (X+dx, Y+dy):
        grid[dx * dy, x, y] += 1
        x+=dx; y+=dy

print((grid[0]>1).sum(), (grid.sum(0)>1).sum())
