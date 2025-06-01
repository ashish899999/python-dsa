nums=[2,3,4,1,1,4,5,1,0,0,0]
M=[89,5,2,1,0]
hash_list=[0]*11

def ret_lsit(nums,M):
    for i in range(len(nums)):
         hash_list[nums[i]]+=1
         
    for z in M:
        if z<1 or z>10:
            print(0)
        else:
            
            print(hash_list[z])

ret_lsit(nums,M)
            
