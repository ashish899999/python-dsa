# similar to frequency array in c++
n=[5,1,2,3,3,4,5]
z=len(n)+1 
hash_list=[0]*z # [ 0,0,0,.....]
for i in range(len(n)):
    hash_list[n[i]]+=1
print(hash_list) # frequency array get created 
