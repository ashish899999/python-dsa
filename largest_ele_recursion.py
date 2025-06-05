# recursive_code for finding largest element in  a array 
nums=[90,3,4,5,99,4,1,23452,-90]
maxi=0
def larg(nums,maxi):
    if(len(nums)==0):
        return maxi
    if(nums[0]>maxi):
        maxi=nums[0]
    return larg(nums[1:len(nums)],maxi)
print(larg(nums,maxi))
