# Robot in a Grid Recursion (CtCI/Chapter_8/8.2)
'''
Imagine a bot sitting on the upper left corner of grid with r rows and c columns. 
The robot can only move in 2 directions, right and down, but certain cells are "off limits" such that the robot cannot step on tgem. 
Design an algorithm to fund a path for the robot from the top left to bottom right
'''

# Setup
''' 
Grid
    1: bad block
    2: bottom right
path: global var to store path
'''

# Idea
'''
Start from top left of the grid
Have row, col, and path as parameters of recurson function
Have a recursion:
    Check if robot goes out of grid or hits bad block   
    If robot ends up at bottom right, return path
    Else
        Increment col by 1 for going to the right and add 'right' to path
        Increment row by 1 for going down and add 'down' to path
'''

# Implement
import time
start_time = 0
grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 2]
]

path_result = ''


def move(row, col, path):
    global path_result
    if (row > 6 or col > 6) or (grid[row][col] == 1):
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
    global start_time
    start_time = time.time()
    move(0, 1, 'right')
    if not path_result == '':
        return path_result
    move(1, 0, 'down')
    if not path_result == '':
        return path_result
    return 'No path found'


result = start()
print(result)
end_time = time.time()
print('total time: ')
print(end_time - start_time)

