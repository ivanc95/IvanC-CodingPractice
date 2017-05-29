#!/usr/bin/python

# Interview Cake Questions: Making Change
#   They found out you're a programmer and asked you to solve something they've been wondering for a long time.
#   Write a function that, given:
#   an amount of money and a list of coin denominations
#   computes the number of ways to make the amount of money with coins of the available denominations.

# Ivan Cordoba

# Initial Thoughts: Create all combinations of elements (can have duplicates) that add up to desired amount

#IN PROGRESS!!!!


def ways(denom, amount):
    denom.sort()
    arr = []
    for i in range(0, len(denom)):
        if amount % denom[i] == 0:
            arr.append([denom[i]] * int(amount/denom[i]))




    return arr

#Begin Testing
denominations = [1, 2, 3]
amount = 4
print ways(denominations, amount)