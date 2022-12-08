import pprint
import time
start_time = time.time()

class XY():
    def __init__(self, coord):
        self.x = int(coord[0])
        self.y = int(coord[1])

class Vent():

    def __init__(self, line):
        self.start, self.end = line.split(' -> ')
        self.start = XY(self.start.split(','))
        self.end = XY(self.end.split(','))

    def print(self):
        print(str(self.start.x) + ',' + str(self.start.y) + ' -> ' + str(self.end.x) + ',' + str(self.end.y))

fin = open("input.txt",mode='r')
grid_size = 1000
##fin = open("test_input.txt",mode='r')
##grid_size = 10

vent_lines = fin.read().split('\n')

fin.close()

vent_lines = [Vent(line) for line in vent_lines]


grid = [[0]*grid_size for i in range(grid_size)]
grid_t = [[0]*grid_size for i in range(grid_size)]

for line in vent_lines:
    #line.print()
    # Vertical
    if line.start.x == line.end.x:
        if line.start.y < line.end.y:
            for y in range(line.start.y,line.end.y + 1):
                grid[line.start.x][y] += 1
        else:
            for y in range(line.start.y,line.end.y - 1, -1):
                grid[line.start.x][y] += 1
    # Horizontal
    elif line.start.y == line.end.y:
        if line.start.x < line.end.x:
            for x in range(line.start.x,line.end.x + 1):
                grid[x][line.end.y] += 1
        else:
            for x in range(line.start.x,line.end.x - 1, -1):
                grid[x][line.end.y] += 1
    # Diagonal
    else:
        if line.start.x < line.end.x:
            # right and up
            if line.start.y < line.end.y:
                line_len = line.end.x - line.start.x + 1
                for i in range(line_len):
                    grid[line.start.x + i][line.start.y + i] += 1
            # right and down
            else:
                line_len = line.end.x - line.start.x + 1
                for i in range(line_len):
                    grid[line.start.x + i][line.start.y - i] += 1

        else:
            # left and up
            if line.start.y < line.end.y:
                line_len = line.start.x - line.end.x + 1
                for i in range(line_len):
                    grid[line.start.x - i][line.start.y + i] += 1
            # left and down
            else:
                line_len = line.start.x - line.end.x + 1
                for i in range(line_len):
                    grid[line.start.x - i][line.start.y - i] += 1
        #continue            
        #print('Skip')
    #pprint.pp(grid)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid_t[j][i] = grid[i][j]
        
#pprint.pp(grid_t)

danger = 0

for row in grid:
    for entry in row:
        if entry >= 2:
            danger += 1

print(danger)
print('execution time:', 1000*(time.time() - start_time), 'milliseconds')
