nums=[1,2,4,0,5,7,8,90]
i=0
j=len(nums)-1
def rev_n(nums,i,j):
    if(i>j):
        return nums
    else:
        nums[i],nums[j]=nums[j],nums[i]
        return rev_n(nums,i+1,j-1)
print(rev_n(nums,i,j))
