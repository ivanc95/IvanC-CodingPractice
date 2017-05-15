#!/usr/bin/python
#Recursive problem
#We discussed this one together briefly

#QUESTION: Print out the path with the weight of heaviest path from start to end

#Input
#1. test_grid = [
# 	[1, 3],
# 	[4, 5],
# ]
#2. x position: 0
#3. y position: 0

#Output
#Down, Right (has weight of 10)

grid = [
	[5, 6, 16, 300, 5],
	[108, 3, 200, 23, 2],
	[110, 37, 89, 180, 89],
	[57, 54, 46, 76, 52],
	[9, 63, 64, 218, 80]
]

def get_max_path(grid, x, y):
    print("temp")

def test():
    get_max_path(grid, 0, 0)

test()
