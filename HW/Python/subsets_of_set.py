#!/usr/bin/python

#Time Complexity: O(log(n^2))
#Space Complexity: O()

#Print out all subsets of a set
#eg
#{x,y} ==> {{}, {x}, {y}, {x,y}} Remember that we are working with sets so {y,x} is not different from {x, y}
#{1,2,3} ==> {{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}
#Input: Set as an array
#Output: Subsets in any order
#Solutions: http://stackoverflow.com/questions/728972/finding-all-the-subsets-of-a-set OR
#http://stackoverflow.com/questions/4640034/calculating-all-of-the-subsets-of-a-set-of-numbers

#Idea: have an output array and and a temporary array, output array will only contain one element initially the empty set.
#      Iterate through input array and create a temporary array that concatenates x from the input array with every set in the output array
#      Concatenate temporary array and output array to create new output array. Use recursion to accomedate for all combinations

test_array = [1, 2, 3, 4]

def subsets(arr, step):
    temp = []       #Temporary array to store new combination
    # Check if at smallest possible combinations and create initial array {{},{1}}
    if step == 0:
        temp.append([])
        temp.append([arr[0]])
        return temp

    r = subsets(arr, step - 1)  #Store returned array with current combinations

    x = len(r)      #store length of r for later use

    #iterate through every element(set) in r
    for i in range(0, x):
        # concatenate current element(index indicated by step) to every set and store in new array
        temp.append(r[i] + [arr[step]])

    #store concatenate running combination with new combinations obtained from for loop
    temp = r + temp

    return temp

temp = subsets(test_array, len(test_array) - 1)
print temp