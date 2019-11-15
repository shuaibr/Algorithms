x = [9,8,7,6,5,1,2,3,4,5,6,7,8]


start = 0
end = len(x)-1

def FindP(start, end, x):
    mid = int((start+end)/2)
    print(start, end, mid)
    if start == end:
        return x[start]
    elif x[mid]>x[mid+1]:
        return FindP(mid+1,end,x)
    elif x[mid] < x[mid+1]:
        if x[mid] > x[mid-1]:
            return FindP(start, mid-1, x)
        elif x[mid] < x[mid-1]:
            return x[mid]
    
print("The answer is : ", FindP(start,end,x))
        
    

