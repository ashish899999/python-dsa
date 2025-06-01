nums=[2,3,4,1,1,4,5,1,0,0,0]
M=[89,5,2,1,0]
hash_map={}
def ret_lst(nums,M):
    for i in range(len(nums)):
         hash_map[nums[i]]=hash_map.get(nums[i],0)+1
    # created dictionary-> O(n)
    for m in M:
        print(hash_map.get(m,0))
        
ret_lst(nums,M) 
