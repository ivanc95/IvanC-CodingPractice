#!/usr/bin/python
#Read up on quicksort and quickselect
#You may want to first implement and understand quicksort before doing this problem.

#Find el of rank 'k' in ascending order given an array

# Input: 2 4 3 1 6, k = 2
# 
# Output: 2

# Input: 3 1 6, k = 2
# Output: 3

import math

test_array = [9, 7, 3, 6, 5, 2, 10, 8, 1, 4]

def partition(arr, low, high, pi):
    i = low
    pivot = arr[pi]
    arr[pi], arr[high] = arr[high], arr[pi]
    for j in range(low, high):
        if (arr[j] < pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]

    pi = arr[int(math.floor((high - low)/2))]
    pi = partition(arr, low, high, pi)

    if k == pi:
        return arr[k]
    elif k < pi:
        return quickselect(arr, low, pi - 1, k)
    else:
        return quickselect(arr, pi + 1, high, k)

hi = len(test_array) - 1
k = 9
sol = quickselect(test_array, 0, hi, k)
print test_array
print sol
