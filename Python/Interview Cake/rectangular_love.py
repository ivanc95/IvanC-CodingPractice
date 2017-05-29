#!/usr/bin/python

# Interview Cake Questions: Rectangular Love
#   Write a function to find the rectangular intersection of two given love rectangles.

# Ivan Cordoba

# Initial Thoughts: Somewhat similar to the overlapping meeting times but only have to account for two rectangles
# Initial Solution(at 38 min mark): Check to see if left_x + width or bottom_y + height overlaps with any part of the other rectangle,
#                   then we can calculate the overlapping rectangle if it does overlap and output in the desired format
#Time Complexity: Runs through code once so only O(1)
#Space Complexity: Only simlple variables created so O(1)

def intersection(rect1, rect2):
    n_left_x = 0
    n_bottom_y = 0
    n_width = 0
    n_height = 0

    #Find Left bound of overlapping rectangle
    if rect2["left_x"] > rect1["left_x"] and rect2["left_x"] < (rect1["left_x"] + rect1["width"]):
        n_left_x = rect2["left_x"]
    elif rect1["left_x"] > rect2["left_x"] and rect1["left_x"] < (rect2["left_x"] + rect2["width"]):
        n_left_x = rect1["left_x"]

    #Find Width of Overlapping rectangle
    if (rect2["left_x"] + rect2["width"]) > rect1["left_x"] and (rect2["left_x"] + rect2["width"]) < (rect1["left_x"] + rect1["width"]):
        n_width = (rect2["left_x"] + rect2["width"]) - rect1["left_x"]
    elif (rect1["left_x"] + rect1["width"]) > rect2["left_x"] and (rect1["left_x"] + rect1["width"]) < (rect2["left_x"] + rect2["width"]):
        n_width = (rect1["left_x"] + rect1["width"]) - rect2["left_x"]

    #Find Bottom bound of overlapping rectangle
    if rect2["bottom_y"] > rect1["bottom_y"] and rect2["bottom_y"] < (rect1["bottom_y"] + rect1["height"]):
        n_bottom_y = rect2["bottom_y"]
    elif rect1["bottom_y"] > rect2["bottom_y"] and rect1["bottom_y"] < (rect2["bottom_y"] + rect2["height"]):
        n_bottom_y = rect1["bottom_y"]

    #Find Heigth of Overlapping rectangle
    if (rect2["bottom_y"] + rect2["height"]) > rect1["bottom_y"] and (rect2["bottom_y"] + rect2["height"]) < (rect1["bottom_y"] + rect1["height"]):
        n_height = (rect2["bottom_y"] + rect2["height"]) - rect1["bottom_y"]
    elif (rect1["bottom_y"] + rect1["height"]) > rect2["bottom_y"] and (rect1["bottom_y"] + rect1["height"]) < (rect2["bottom_y"] + rect2["height"]):
        n_height = (rect1["bottom_y"] + rect1["height"]) - rect2["bottom_y"]

    my_rectangle_out = {

        # coordinates of bottom-left corner
        'left_x': n_left_x,
        'bottom_y': n_bottom_y,

        # width and height
        'width': n_width,
        'height': n_height,

    }

    return my_rectangle_out


#Beign testing

my_rectangle_1 = {

    # coordinates of bottom-left corner
    'left_x': 0,
    'bottom_y': 0,

    # width and height
    'width': 4,
    'height': 4,

}

my_rectangle_2 = {

    # coordinates of bottom-left corner
    'left_x': 2,
    'bottom_y': 4,

    # width and height
    'width': 4,
    'height': 4,

}

print intersection(my_rectangle_1, my_rectangle_2)


