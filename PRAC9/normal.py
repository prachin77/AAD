# NORMAL KNAPSACK 

# formula
# table[i,j] = max{table[i-1,j] , v[i] + table[i-1,j-w[i]]} ; if j >= w[i]
# table[i,j] = table[i-1,j] ; if j < w[i]

# import numpy as np

# def Calculate_Knapsack(max_weight,w,v):
#     m , n = len(w) , len(v)
#     table = np.zeros((m+1,max_weight+1),dtype=int)
#     items = {}

#     for i in range(1,m+1):
#         for j in range(1,max_weight+1):
#             if(j >= w[i-1]):
#                 table[i,j] = max(table[i-1,j] , v[i-1] + table[i-1,j-w[i-1]])
#             elif(j < w[i-1]):
#                 table[i,j] = table[i-1,j]

#     print(table)

#     i,j = m,max_weight
#     while i>0 and j>0:
#         if(table[i,j] == table[i-1,j]):
#             i=i-1
#         elif(table[i,j] != table[i-1,j]):
#             items[i] = [v[i-1], w[i-1]]
#             j=j-w[i-1]
#             i=i-1

#     print(f"items included [item_no : value , weight] = {items}")

# max_weight = 5
# weights = [2,3,4,5]
# values = [3,4,5,6]
# Calculate_Knapsack(max_weight,weights,values)



# FRACTIONAL KNAPSACK
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def ratio(item):
    return item.profit / item.weight

def FractionalKnapsack(W,arr):
    max_profit=0
    arr.sort(key=ratio, reverse=True)

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            max_profit += item.profit
        else:
            max_profit += item.profit * (W / item.weight)
            break  

    return max_profit


if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]

    max_val = FractionalKnapsack(W, arr)
    print(f"max profit : {max_val}")