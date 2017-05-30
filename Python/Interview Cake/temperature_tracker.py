#!/usr/bin/python
# -*- coding: utf-8 -*-

# Interview Cake Questions: Temperature Tracker
#   Write a class TempTracker with these methods:
#       insert()—records a new temperature
#       get_max()—returns the highest temp we've seen so far
#       get_min()—returns the lowest temp we've seen so far
#       get_mean()—returns the mean ↴ of all temps we've seen so far
#       get_mode()—returns a mode ↴ of all temps we've seen so far


# Initital Thoughts: Kept Track of all values and updated as inserted, Used dictionary(hash map) to keep track of mode
#                    had to look up how definitions work in python


# Time Complexity: instert() is O(n) due to mapping while all get_X() functions are O(1)
#
# Space Complexity: O(n)? their is one data structure that expands based on number of inserts


# Ivan Cordoba
class TempTracker:
    def __init__(self):
        self.temps = []
        self.counts = {}
        self.sum = 0
        self.max = -1
        self.min = 111
        self.mean = 0
        self.mode = 0

    def insert(self, new_temp):
        self.temps.append(new_temp)

        self.max = max(self.max, new_temp)      #Update Max Value

        self.min = min(self.min, new_temp)      #Update Min Value

        self.sum = self.sum + new_temp          #Update Mean
        self.mean = self.sum/len(self.temps)

        if new_temp in self.counts:
            self.counts[new_temp] = self.counts[new_temp] + 1
        elif len(self.counts) == 0:
            self.counts[new_temp] = 1
            self.mode = new_temp
        else:
            self.counts[new_temp] = 1

        if self.counts[new_temp] > self.counts[self.mode]:
            self.mode = new_temp


    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode

#Begin Testing
tt = TempTracker()
tt.insert(10)
tt.insert(70)
tt.insert(101)
tt.insert(7)
tt.insert(90)
tt.insert(70)
print "Max: " +  str(tt.get_max())
print "Min: " + str(tt.get_min())
print "Mean: " + str(tt.get_mean())
print "Mode: " + str(tt.get_mode())
