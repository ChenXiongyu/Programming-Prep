
# These are code chunks from the Homework 2 instructions,
# so that you can copy-and-paste and do less typing yourself


# 1.a

import numpy as np

np.random.seed(1)   # so results match

list1 = [2, -4, 7, 2, 0, 5, -3, 4, -2]
print("max_sublist_sum(", list1,
               "): ", max_sublist_sum(list1))

for n in range(10, 20):
    listn = list(np.random.randint(-5, 9, size=n))
    print("max_sublist_sum(", listn,
                   "): ", max_sublist_sum(listn))


# 1.b

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



# 2.a

print('18 in bt3:', 18 in bt3)
print('21 in bt3:', 21 in bt3)
print('13 in bt1:', 13 in bt1)
print('13 in bt3:', 13 in bt2)


# 2.b

bt3r = bt3           # copy or reference?
print('\nbt3r.print_pretty():')
bt3r.print_pretty()
print('bt3r == bt3:', bt3r == bt3)
print('bt3r is bt3:', bt3r is bt3)
bt3c = bt3.copy()    # copy or reference?
print('\nbt3c.print_pretty():')
bt3c.print_pretty()
print('bt3c == bt3:', bt3c == bt3)
print('bt3c is bt3:', bt3c is bt3)


# 2.c

bt3c.negate()
print('\nbt3c.print_pretty():')
bt3c.print_pretty()

