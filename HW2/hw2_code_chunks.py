
# These are code chunks from the Homework 2 instructions,
# so that you can copy-and-paste and do less typing yourself


# 1.a

import numpy as np

np.random.seed(1)   # so results match


def max_sublist_sum(l):
    start = 0
    end = 1
    for i in range(1, len(l)):
        if sum(l[end:i + 1]) > 0:
            end = i + 1
            if sum(l[start:i]) < 0:
                start = i
        else:
            continue
    return sum(l[start:end])
    
    
# list1 = [2, -4, 7, 2, 0, 5, -3, 4, -2]
# print("max_sublist_sum(", list1,
#                "): ", max_sublist_sum(list1))

# for n in range(10, 20):
#     listn = list(np.random.randint(-5, 9, size=n))
#     print("max_sublist_sum(", listn,
#                    "): ", max_sublist_sum(listn))


# 1.b
def knapsack01(item_wgts, item_vals, tot_wgt):
    A = np.zeros((len(item_wgts) + 1, tot_wgt + 1), dtype=int)
    for k in range(1, len(item_wgts) + 1):
        for X in range(1, tot_wgt + 1):
            if X - item_wgts[k - 1] < 0:
                A[k, X] = A[k - 1, X]
            else:
                A[k, X] = max(A[k - 1, X], 
                              item_vals[k - 1] + A[k - 1, X - item_wgts[k - 1]])
    return A[-1, -1]


# item_weights = [3, 1, 12, 5, 2]
# item_values = [9, 7, 18, 3, 11]
# total_weight = 10

# print("max value:",
#         knapsack01(item_weights, item_values,
#                    total_weight))
 

# item_weights = [2, 3, 5, 1, 12]
# item_values = [11, 9, 3, 7, 18]
# total_weight = 10

# print("max value:",
#         knapsack01(item_weights, item_values,
#                    total_weight))
 

# item_weights = [2, 4, 9, 3, 12, 4, 1, 3]
# item_values = [8, 4, 2, 11, 9, 5, 2, 8]
# total_weight = 20

# print("max value:",
#         knapsack01(item_weights, item_values,
#                    total_weight))


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


# coins = [2, 3, 6]
# value = 10

# print("value", value, "requires",
#            min_coins(coins, value), "coins minimum")
 


# coins = [1, 5, 10, 25]
# value = 117

# print("value", value, "requires",
#            min_coins(coins, value), "coins minimum")
 


# coins = [1, 5, 10, 18, 25, 37]
# value = 273

# print("value", value, "requires",
#            min_coins(coins, value), "coins minimum")



# # 2.a

# print('18 in bt3:', 18 in bt3)
# print('21 in bt3:', 21 in bt3)
# print('13 in bt1:', 13 in bt1)
# print('13 in bt3:', 13 in bt2)


# # 2.b

# bt3r = bt3           # copy or reference?
# print('\nbt3r.print_pretty():')
# bt3r.print_pretty()
# print('bt3r == bt3:', bt3r == bt3)
# print('bt3r is bt3:', bt3r is bt3)
# bt3c = bt3.copy()    # copy or reference?
# print('\nbt3c.print_pretty():')
# bt3c.print_pretty()
# print('bt3c == bt3:', bt3c == bt3)
# print('bt3c is bt3:', bt3c is bt3)


# # 2.c

# bt3c.negate()
# print('\nbt3c.print_pretty():')
# bt3c.print_pretty()

