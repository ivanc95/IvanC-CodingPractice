#!/usr/bin/python

#Time Complexity: O(log(n^2)), actually O(n^2)
#Space Complexity: O()

# Read up on quicksort and quickselect
# You may want to first implement and understand quicksort before doing this problem.

# Find el of rank 'k' in ascending order given an array

# Input: 2 4 3 1 6, k = 2
# Output: 2

# Input: 3 1 6, k = 2
# Output: 3

test_array = [9, 7, 3, 6, 5, 2, 10, 8, 1, 4]

#partition around rightmost point in the section
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if (arr[j] <= pivot):
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

#quicksort implementation
def quicksort(arr, low, high):
    #only do something if low < high
    if (low < high):
        pi = partition(arr, low, high) #get pivot index from partitiono function
        quicksort(arr, low, pi - 1) #call quicksort for all elements less than pivot index
        quicksort(arr, pi + 1, high) #call quicksort for all elements greater than pivot index


hi = len(test_array) - 1
quicksort(test_array, 0, hi)
print(test_array)