# Robot in a Grid (CtCI/Chapter_8/8.2)

'''
Imagine a bot sitting on the upper left corner of grid with r rows and c columns. 
The robot can only move in 2 directions, right and down, but certain cells are "off limits" such that the robot cannot step on tgem. 
Design an algorithm to fund a path for the robot from the top left to bottom right
'''


''' 
1: bad block
2: bottom right
'''

#  Recursion solution
grid = [
    [0, 0, 1],
    [1, 0, 1],
    [1, 0, 2]
]

path_result = ''


def move(row, col, path):
    global path_result
    if (row > 2 or col > 2) or (grid[row][col] == 1):
        return
    elif grid[row][col] == 2:
        path_result = path
        return
    else:
        # go right
        move(row, col+1, path + ' right')
        # go down
        move(row+1, col, path + ' down')


def start():
    move(0, 1, 'right')
    if not path_result == '':
        return path_result
    move(1, 0, 'down')
    if not path_result == '':
        return path_result
    return 'No path found'


result = start()
print(result)

