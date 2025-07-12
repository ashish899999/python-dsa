# bubble sort
nums=[9,20,0,1,-1,877]
for i in range(len(nums)):
    flag=False
    for j in range(1,len(nums)-i):
        if(nums[j-1]>nums[j]):
            flag=True
            nums[j-1],nums[j]=nums[j],nums[j-1]
    if(flag==False):
        break
print(nums)

# worst case 
# swaps= n(n-1)//2, => O(N^2) in worst case 
#comparison = n(n-1)/2=> O(n^2) in wore case
# swaps=O(1) in best case
# comparison =O(N-1) in best case
# bubble sort is both inplace and stable 
