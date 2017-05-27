#!/usr/bin/python

# Interview Cake Questions: Highest Product of 3
#   Given a list of integers, find the highest product you can get from three of the integers.
#   The input list_of_ints will always have at least three integers.

# Ivan Cordoba

# Initial Thoughts: Product of all combinations of 3 numbers in array
# Initial Solution: Sort list and take product of 3 largest numbers, product should be largest possible in array

# Second Solution: Instead of sorting iterate through list once to find 3 biggest and 2 smallest numbers

# Initial Solution: O(nlog(n))
def highest_product_init(arr):
    arr.sort()#sort array
    first = arr[0] * arr[1]
    last = arr[-2] * arr[-3]
    if first > last:
        return arr[-1] * first
    return arr[-1] * last

# Second Solution: O(n)
def highest_product(arr):
    s1 = 0
    s2 = 0
    l1 = 0
    l2 = 0
    l3 = 0
    for i in range(0, len(arr)):
        if arr[i] < s1:
            s2 = s1
            s1 = arr[i]
        elif arr[i] < s2:
            s2 = arr[i]

        if arr[i] > l3:
            l1 = l2
            l2 = l3
            l3 = arr[i]
        elif arr[i] > l2:
            l1 = l2
            l2 = arr[i]
        elif arr[i] > l1:
            l1 = arr[i]

    first = s1 * s2
    last = l1 * l2
    if first > last:
        return l3 * first
    return l3 * last


# Begin Testing
nums = [-10, -8, 1, 3, 4, 5, 7]
print highest_product(nums)