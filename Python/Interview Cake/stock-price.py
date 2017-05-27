#!/usr/bin/python

# Interview Cake Questions: Apple Stock
#  Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made
#  from 1 purchase and 1 sale of 1 Apple stock yesterday.

# Ivan Cordoba

# Initial Thoughts: We want to find the greatest value of (arr[y] - arr[x]) where (y > x)
# Initial Solution(finished at 21 min mark): Nested for loop that will search through list to find differences

# Secondary Thoughts: You can keep track of the minimum you run through the list once,
#                     I initially ruled this out (not sure why) so it took me a while to figure this out

# Space Complexity: No new data structures created so O(1) on both solutions

#Initial Solution, not very efficient but it works: O(n^2)
def get_max_profit_init(arr):
    buy_index = -1
    sell_index = -1
    profit = 0
    profit_new = 0;
    #Loop throrugh every element except last
    for i in range(0, len(arr) - 1):
        #Loop through from i+1 to end
        for j in range(i + 1, len(arr)):
            profit_new = arr[j] - arr[i]    #New profit for iteration
            # If new profit is greater than current -> update values (profit, sell_index, buy_index)
            if (profit_new) > profit:
                profit = profit_new
                sell_index = j
                buy_index = i

    return buy_index, sell_index, profit

#Beter solution, only runsr through list once: O(n)
def get_max_profit(arr):
    min_index = 0
    profit = arr[1] - arr[0]
    profit_new = 0
    for i in range(1, len(arr)):
        profit_new = arr[i] - arr[min_index]
        if profit_new > profit:
            profit = profit_new
        if arr[i] < arr[min_index]:
            min_index = i
    return profit



#Begin Testing Process
stock_prices_yesterday = [10, 13, 5, 8, 11, 9, 12]
print "Max profit of " + str(get_max_profit(stock_prices_yesterday))
# b, s, p = get_max_profit_init(stock_prices_yesterday)
# print "Buy stock at: " + str(b)
# print "Sell stock at: " + str(s)
# print "Profit of: " + str(p)


