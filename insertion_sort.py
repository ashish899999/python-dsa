# insertion sort
nums=[9,20,0,1,-1,877]
for i in range(1,len(nums)):
    key=nums[i]
    j=i-1
    while(j>=0 and nums[j]>key):
        nums[j+1]=nums[j]
        j=j-1
    nums[j+1]=key
print(nums)
# insertion sort 
# best case comparison is n-1 =O(N)
# worst case comparison is n(n-1)/2=o(n^2)
# swaps in best case is o(1)
# swpas in worst case is o(n^2)
# insertion sort is both stable and inplace 
