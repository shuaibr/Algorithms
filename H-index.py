x = [0,41,23,12,6,6,5,4,3,2,2]
start = 1
end = len(x)
n = len(x)

def hIndex(start, end, c):
    mid = int((start + end)/2)
    print(c[mid], " ", mid)
    if start == end:
        return mid
    elif (c[mid] == (mid)):
        return mid
    elif (c[mid] <(mid)):
        return hIndex(start, mid-1,c)
    else:
        return hIndex(mid+1, end,c)
    return False 

print("K = ", hIndex(start, end, x))
    

