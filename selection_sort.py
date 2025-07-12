# selection sort
nums=[9,20,0,1,-1,877]
for i in range(len(nums)):
    current_index=i
    for j in range(i+1,len(nums)):
        if(nums[j]<nums[current_index]):
            current_index=j
    if(current_index!=i):
        nums[i],nums[current_index]=nums[current_index],nums[i]
        
print(nums)
# selection sort
# swaps is O(N) in worst case 
# swaos in o(1) in best case
# comparison is o(n^2) in both best and worst case
# selecition sort is inplce but not a stable algo 
# here we are finding min in each unsorted array
