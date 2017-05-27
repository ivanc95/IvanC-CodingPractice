#!/usr/bin/python

#Let's say a meeting is stored as tuples of integers (start_time, end_time).
# These integers represent the number of 30-minute blocks past #9:00am.
#For example:


#Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges.
#For example:
#Input:   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#Output:   [(0, 1), (3, 8), (9, 12)]

#Do not assume the meetings are in order

#Idea 1: Iterate through array comparing each element to every other element,
#        Combine if conditions met, restart search until no elements can be combined

#Looked up: deleting element(s) from an array

def sort_array(arr):

    return arr

def merge_ranges(arr):

    #sort array

    temp = []

    for i in range(len(arr)):
        s, e = arr[i]
        sn, en = arr[i + 1]

        if s <= sn and s >= en:
            temp.append((sn, e))
        elif e >= sn and e <= en:
            temp.append((s, en))
        else:
            temp.append(s, e)



    return arr




input = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print merge_ranges(input)