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

def merge_ranges(arr):

    done = False
    while not done:
        done = True
        for i in range(0, len(arr)):
            s, e = arr[i]
            for j in range(0, len(arr)):
                sc, ec = arr[j]
                if i != j and s <= ec and s >= sc:
                    if i > j:
                        del arr[i]
                        del arr[j]
                    else:
                        del arr[j]
                        del arr[i]
                    arr.append((sc, e))
                    done = False
                    break
                elif i != j and e >= sc and e <= ec:
                    if i > j:
                        del arr[i]
                        del arr[j]
                    else:
                        del arr[j]
                        del arr[i]
                    arr.append((s, ec))
                    done = False
                    break

            if not done:
                break
    return arr




input = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print merge_ranges(input)