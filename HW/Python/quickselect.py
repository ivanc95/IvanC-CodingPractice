#!/usr/bin/python

#Time Complexity: O(log(n))
#Space Complexity: O()

#Read up on quicksort and quickselect
#You may want to first implement and understand quicksort before doing this problem.

#Find el of rank 'k' in ascending order given an array

# Input: 2 4 3 1 6, k = 2
# 
# Output: 2

# Input: 3 1 6, k = 2
# Output: 3

#Defenition: Use same approach as quicksort but only use partition that contains index of solution
#            results in partially sorted list with kth element in right place

# imported math to use floor function
import math

test_array = [9, 7, 3, 6, 5, 2, 10, 8, 1, 4]

#partition array around pivot point, values less than to left and greater than to right
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

#recursive quick select algorithm
def quickselect(arr, low, high, k):
    #return element if section is only 1 element long
    if low == high:
        return arr[low]

    # pivot index equal to mid point of section
    pi = arr[int(math.floor((high - low)/2))]
    # update pivot index from call of partition function
    pi = partition(arr, low, high, pi)

    # if kth element is pivot index then return kth element of array
    if k == pi:
        return arr[k]
    # if k is less than pivot index then take low(left) part of the partition
    elif k < pi:
        return quickselect(arr, low, pi - 1, k)
    # if k is greater than or equal to pivot index take high(right) part of partition
    else:
        return quickselect(arr, pi + 1, high, k)

#initialization of variables and function call
hi = len(test_array) - 1
k = 9
sol = quickselect(test_array, 0, hi, k)
print test_array
print sol
