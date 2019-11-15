x = [-2,-10,2,-4,-5,5,6]
point_i = 0
j = 0

print("OG is ", x)

while point_i<len(x):
    if x[point_i]<0:
        temp = x[point_i]
        x[point_i] = x[j]
        x[j] = temp
        j+=1
    point_i+=1

print("Final answer is ", x)
    

