nums=[1,3,1,4,5,1,1]
hash_map={}
for i in range(len(nums)):
  hash_map[nums[i]]=hash_map.get(nums[i],0)+1
print(hash_map)
  
  
