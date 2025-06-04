nums=[1,2,4,5,7,8]
i,j=0,len(nums)-1
while(i<j):
    nums[i],nums[j]=nums[j],nums[i]
    i,j=i+1,j-1
print(nums)
