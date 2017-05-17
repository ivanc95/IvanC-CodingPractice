#!/usr/bin/python

#Time Complexity: O(log(n))
#Space Complexity: O()

#Recursive problem
#We discussed this one together briefly

#QUESTION: Print out the path with the weight of heaviest path from start to end

#Input
#1. test_grid = [
# 	[1, 3],
# 	[4, 5],
# ]
#2. x position: 0 | x is column number
#3. y position: 0 | y is row number

#Output
#Down, Right (has weight of 10)


#Idea 1: Original thought was to build a tree of all possible paths and then use that to get solution
#Idea 2: Build a recursive function that checks both left and down and returns the 'max' of the two if a node that
#        is not the goal node is checked run function on that nodes children until goal node is reached

grid = [
	[5, 6, 16, 300, 5],
	[108, 3, 200, 23, 2],
	[110, 37, 89, 180, 89],
	[57, 54, 46, 76, 52],
	[9, 63, 64, 218, 80]
]

test_grid = [
	[1, 3],
	[4, 5]
]

def get_max_path(grid, x, y):
    #initialize variables
    x_size = len(grid[0])
    y_size = len(grid)
    xn = x + 1
    yn = y + 1
    down_return = 0
    right_return = 0
    max = 0
    pathR = ""
    pathD = ""
    #check if at goal coordinates
    if(x == x_size - 1 and y == y_size - 1):
        return "", grid[y][x]

    #check if at right edge
    if(x < x_size - 1):
        pathR, right_return = get_max_path(grid, x + 1, y)

    #check if at bottom edge
    if(y < y_size - 1):
        pathD, down_return = get_max_path(grid, x, y + 1)

    #see which path has the max weight so far
    if(right_return > down_return):
        max = right_return
        path = "right " + pathR
    elif(right_return <= down_return):
        max = down_return
        path = "down " + pathD

    return path, grid[y][x] + max

def test():
    path, max = get_max_path(grid, 0, 0)
    print("Path Cost: " + str(max))
    print("Path Steps: " + path)

test()
