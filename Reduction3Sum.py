def Fast3Sum(A):
    A.sort()
    for k in range(len(A)):
        x = Sorted2Sum(A, -A[k])
        if x:
            print(x)
            return True
        
    return False

def Sorted2Sum(A,m):
    i = 0
    j = len(A)

    while i <= j:
        if A[i] + A[j] == m:
            return True 
        else:
            if A[i] + A[j] < m:
                i +=1
            else:
                k -=1
    return False 

A = [-1,-2,3,4,5,-5,4,-3]
T = 2

B = []

for i in range(len(A)):
    B.append(A[i]/3-T)

Fast3Sum(B)



    


