#!/usr/bin/python
# Read up on quicksort and quickselect
# You may want to first implement and understand quicksort before doing this problem.

# Find el of rank 'k' in ascending order given an array

# Input: 2 4 3 1 6, k = 2
#
# Output: 2

# Input: 3 1 6, k = 2
# Output: 3

test_array = [9, 7, 3, 6, 5, 2, 10, 8, 1, 4]


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if (arr[j] <= pivot):
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if (low < high):
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


hi = len(test_array) - 1
quicksort(test_array, 0, hi)
print(test_array)