#!/usr/bin/python

# Interview Cake Questions: Product of All Other Numbers
#   Write a function get_products_of_all_ints_except_at_index()
#   that takes a list of integers and returns a list of the products.

# Ivan Cordoba

# Initial Thoughts: Need to multiply all numbers together except current number
# Initial Solution(finished at 10 min mark): Nested for loops, iterates through list and on each iteration iterate through list
#                   and take product of all other numbers, runs in O(n^2) so not very efficient

# Second Solution(finished at 20 min mark): Store running product of all previous numbers, reduces # of iterations

# Third Solution(finished at 50 min mark: Iterate through once to get product of all elements before element at index x,
#                 store running product at index x in new array. Iterate through array a second time but backwards
#                 to get the product of all elements after current element and store in another array like first one.
#                 Finally multiply both arrays together arr1[x]*arr2[x] to get answer

# Space Complexity: All solutions only create one new data structure of size n so O(n)


#Initial Solution: O(n^2)
def products_init(arr):
    prod_arr = []
    for i in range(0, len(arr)):        #Iterate through all elements
        prod = 1
        for j in range(0, len(arr)):    #Iterate through all elments again
            if i != j:                  #Do nothing if i == j
                prod = prod * arr[j]
        prod_arr.append(prod)           #Append final product to output array
    return prod_arr

#Second Solution: O(n^2)
def products_2(arr):
    prod_arr = []
    prod_prev = 1                       #initialize running product of previous elements
    for i in range(0, len(arr)):        #Iterate through all elements
        prod = prod_prev                #Set current product as product of previous elemrnts
        for j in range(i + 1, len(arr)):#Iterate through all elements after current and update product
            prod = prod * arr[j]
        prod_arr.append(prod)           #Append final product to output array
        prod_prev = prod_prev * arr[i]  #Update running product of all previous elements

    return prod_arr

#Third Solution: Iterates through list twice O(2*n) -> O(n)
def get_products_of_all_ints_except_at_index(arr):
    prod_arr = []
    prod_prev = 1                       # initialize running product of previous elements
    for i in range(0, len(arr)):        # Iterate through all elements
        prod_arr.append(prod_prev)      # Append final product to output array
        prod_prev = prod_prev * arr[i]  # Update running product of all previous elements

    prod_prev = 1                       # initialize running product of previous elements
    for i in range(len(arr) - 1, -1, -1):    # Iterate through all elements backwards
        prod_arr[i] = prod_arr[i] * prod_prev
        prod_prev = prod_prev * arr[i]

    return prod_arr


#Begin testing
nums = [1, 7, 3, 4]
print get_products_of_all_ints_except_at_index(nums)

