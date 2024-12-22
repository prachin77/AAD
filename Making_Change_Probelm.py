# formulas:
# if    i=1    then  m[i,j] = 1 + m[1,j-d1]
# if    j<d[i] then  m[i,j] = m[[i-1,j]]
# else  m[i,j] = min(m[i-1,j] , 1 + m[i,j-d[i]])

import numpy as np

class MakingChange:
    def __init__(self , total_amt , coins):
        self.coin_list_len = len(coins)
        self.total_amt = total_amt
        self.coins = coins

    def MakingChangeTable(self):
        m = np.zeros((self.coin_list_len , self.total_amt+1))

        for i in range(self.coin_list_len):
            m[i][0] = 0

        for i in range(1,self.coin_list_len+1):
            for j in range(0,self.total_amt+1):
                if(i == 1):
                    if j >= self.coins[0]:  
                        m[i-1][j] = 1 + m[i-1][j - self.coins[0]] 
                elif(j < self.coins[i-1]):
                    m[i-1][j] = m[i-2,j]
                else:
                    m[i-1][j] = min(m[i-2,j] , 1+m[i-1,j-self.coins[i-1]])

        return m        

    def SolveMakingChange(self):
        coins_used = []
        m = self.MakingChangeTable()

        print("TABLE")
        print(m)

        i = self.coin_list_len - 1 
        j = self.total_amt

        while j > 0 and i >= 0:
            if(i == 0 or m[i][j] != m[i - 1][j]):  
                coins_used.append(self.coins[i])  
                j -= self.coins[i]  
            else:
                i -= 1  

        total = sum(coins_used)

        if total == self.total_amt:
            print("coins used = ",coins_used)
            print("no of coins = ",len(coins_used))        
        else:
            print("no solution")

if __name__ == "__main__":
    total_amt = 8
    coins = [1,4,6]

    mc = MakingChange(total_amt , coins)
    mc.SolveMakingChange()

