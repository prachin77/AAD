# 15, 5, -20, 30, -45 -> 15, -20
# 15, 5, -20, 30, 25 -> 15, -20 & -20, 25


arr = []
for i in range(5):
    inp = int(input("enter number : "))
    arr.append(inp)

print(arr)


tmp = float('inf')
num_arr = ()

for i in range(len(arr)):
    for j in range(i,len(arr)):
        n1 = arr[i]
        n2 = arr[j]
        sum = n1 + n2

        if abs(sum) < abs(tmp):
            tmp = sum
            num_arr = (n1,n2)
    sum = 0

print(f"sum of 2 numbers whose addition is closest to 0 : {num_arr}")