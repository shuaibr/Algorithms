# A2Q2

A = [7,6,5,4,3,2,9]
l = 0
r = len(A) - 1
m = 0

def CLS_max(A,l,r,m): 
    while (l<= r):
        m = int((l+r)/2)
        print(m)
        if A[m]>A[m-1]:
            print("Max value: ", A[m])
            return A[m]
        else:
            if A[l]< A[r]:
                if A[l]> A[m]:
                    l=m
                else:
                    r = m
            else:
                if A[l]< A[m]:
                    l=m
                else:
                    r = m

    print(l,r,m) 
#CLS_max(A,l,r,m) 

def find_max(A):
    l=0
    r = len(A)-1
    
    while l<r:
        m = (l+r)//2
        if r == l+1:
            if (A[r]>A[l]):
                return A[r]
            else:
                return A[l]
        elif A[m]> A[r]:
            r = m
            
        elif A[m]<A[r]:
            l = m
print(find_max(A) )
