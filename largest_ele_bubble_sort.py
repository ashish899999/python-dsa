# find largest ele in array
nums=[40,90,10,30,1,2,56]
# one pass of bubble sort and print nums[len(numss)-1]
for i in range(len(nums)-1):
    if(nums[i]>nums[i+1] and i+1<=len(nums)-1):
        nums[i],nums[i+1]=nums[i+1],nums[i]
print(nums)
print(nums[len(nums)-1])
