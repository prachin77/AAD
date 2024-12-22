chef1 = []
chef2 = []

max_no = 3
for i in range(max_no):
    chef1Input = int(input(f"enter index {i} for chef1 : "))
    chef2Input = int(input(f"enter index {i} for chef2 : "))
    print("\n")

    chef1.append(chef1Input)
    chef2.append(chef2Input)

print("chef 1 array : ",chef1)
print("chef 2 array : ",chef2)

chef1Points = 0
chef2Points = 0


for i in range(len(chef1)):
    if(chef1[i] > chef2[i]):
        chef1Points += 1
    elif(chef1[i] < chef2[i]):
        chef2Points += 1
    elif(chef1[i] == chef2[i]):
        pass

print(f"chef 1 points : {chef1Points}")
print(f"chef 2 points : {chef2Points}")