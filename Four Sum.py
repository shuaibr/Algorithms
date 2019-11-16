# CP312 A2Q1 - 4Sum Problem

#slow 
def foursum():

    nums = [1,2,0,-1,-2,0]
    array_len = len(nums)

    target = 0
    result = [] 
    i = 0

    nums.sort() 
    for i in range(array_len-3):
        if i!=0 and nums[i]==nums[i-1]:
            continue
        x = i+1
        for j in range(x, array_len-2):
            if j!= i+1 and nums[j]== nums[j-1]:
                continue
            left = j+1
            right = array_len-1
            
            while left < right:
                sum = nums[i] + nums[j]+ nums[left] + nums[right]

                if sum > target:
                    right -=1
                elif sum < target:
                    left+=1
                else:
                    result.append([nums[i],nums[j], nums[left], nums[right]])
                    left +=1
                    right -=1

                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    while right<right and nums[right]==nums[right+1]:
                        right+=1
    print(result) 
    return result 
                    
#fast
