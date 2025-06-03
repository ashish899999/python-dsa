nums=[1,2,2,1,56]
current_sum=0
def rsum(nums,current_sum):
    if(len(nums)==0):
        return current_sum
    return rsum(nums[1:],current_sum+nums[0])

print(rsum(nums,0))
