# finding 2nd largest element in a array
nums=[90,3,4,123,12,89,34]
# 2 pass laga do bubble sort ka 
for j in range(2):
    for i in range(len(nums)-j-1):
        if(nums[i]>nums[i+1] and i+1<=len(nums)-1):
            nums[i],nums[i+1]=nums[i+1],nums[i]
# ye ek pass ho gya 
print("largest ele is ", nums[len(nums)-1])
print("2nd largest ele is ",nums[len(nums)-2])
