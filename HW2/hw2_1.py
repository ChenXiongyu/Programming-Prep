
# File hw2_1.py
# Author(s): xiongyuc, diwend, yuxuanl5

# 1.a

import numpy as np

np.random.seed(1)   # so results match


def max_sublist_sum(nums):
    l,r  = 0,0
    max_rev = nums[0]
    if len(nums) == 1:
        return max_rev
    for r in range(1, len(nums)):
        max_rev = max(nums[r], max_rev, sum(nums[l:r])+nums[r])
        if max_rev == nums[r]:
            l = r
    return max_rev
    
    
list1 = [2, -4, 7, 2, 0, 5, -3, 4, -2]
print("max_sublist_sum(", list1,
               "): ", max_sublist_sum(list1))

for n in range(10, 20):
    listn = list(np.random.randint(-5, 9, size=n))
    print("max_sublist_sum(", listn,
                   "): ", max_sublist_sum(listn))


# 1.b
def knapsack01(item_wgts, item_vals, tot_wgt):
    dp_matrix = np.zeros((len(item_wgts), tot_wgt+1), dtype=int)
    dp_matrix[0, item_wgts[0]:] = item_vals[0]
    for i in range(1, len(item_wgts)):
        for j in range(tot_wgt+1):
            wgt = item_wgts[i]
            if j - wgt < 0:
                dp_matrix[i,j] = dp_matrix[i-1, j]
            else:
                dp_matrix[i,j] = max(dp_matrix[i-1,j], dp_matrix[i-1,j-wgt] + item_vals[i])
    # print(dp_matrix)
    return(dp_matrix[-1,-1])


item_weights = [3, 1, 12, 5, 2]
item_values = [9, 7, 18, 3, 11]
total_weight = 10

print("max value:",
        knapsack01(item_weights, item_values,
                   total_weight))
 

item_weights = [2, 3, 5, 1, 12]
item_values = [11, 9, 3, 7, 18]
total_weight = 10

print("max value:",
        knapsack01(item_weights, item_values,
                   total_weight))
 

item_weights = [2, 4, 9, 3, 12, 4, 1, 3]
item_values = [8, 4, 2, 11, 9, 5, 2, 8]
total_weight = 20

print("max value:",
        knapsack01(item_weights, item_values,
                   total_weight))


# 1.c
def min_coins(coins, value):
    A = np.array(np.ones(value + 1) * (value + 1), dtype=int)
    for c in coins:
        if c <= value:
            A[c] = 1
        for j in range(c, value + 1):
            A[j] = min(A[j], 1 + A[j - c])
    if A[value] < value + 1:
        return A[value]
    else:
        return -1


coins = [2, 3, 6]
value = 10

print("value", value, "requires",
           min_coins(coins, value), "coins minimum")
 


coins = [1, 5, 10, 25]
value = 117

print("value", value, "requires",
           min_coins(coins, value), "coins minimum")
 


coins = [1, 5, 10, 18, 25, 37]
value = 273

print("value", value, "requires",
           min_coins(coins, value), "coins minimum")
