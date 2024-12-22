import numpy as np


def Calculate_lcs(s1,s2):
    m = len(s1) # m,l,n,o,m
    n = len(s2) # m,n,o,m   
    lcs_sequence = []

    matrix = np.zeros((m+1,n+1),dtype=object)
    arrow_matrix = np.zeros((m+1,n+1),dtype=object)
    

    for i in range(1,m+1):
        for j in range(1,n+1):
            if(s1[i-1] == s2[j-1]):
                matrix[i,j] = matrix[i-1,j-1]+1
                arrow_matrix[i, j] = "↖" 
            elif(matrix[i-1,j] >= matrix[i,j-1]):
                matrix[i, j] = matrix[i - 1, j]
                arrow_matrix[i, j] = "↑"
            else:
                matrix[i, j] = matrix[i, j - 1]
                arrow_matrix[i, j] = "←"

    print(matrix)
    print(arrow_matrix)

    i,j = m,n
    while i>0 and j>0:
        if(arrow_matrix[i,j] == "↖"):
            lcs_sequence.append(s1[i-1])
            i=i-1
            j=j-1
        elif(arrow_matrix[i,j] == "↑"):
            i=i-1
        elif(arrow_matrix[i,j] == "←"):
            j=j-1

    print(f"LCS sequence : {lcs_sequence}")

s1 = input("enter comma seprated values for string 1 : ").split(",")
s2 = input("enter comma seprated values for string 2 : ").split(",")
print(f"string 1 = {s1}")
print(f"string 2 = {s2}")


Calculate_lcs(s1,s2)