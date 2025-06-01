s="aaaabccdd"
q=["a","c"]
# a better freq array method
hash_list=[0]*27
for char in s:
    ascii_value=ord(char)
    index=ascii_value-97
    hash_list[index]+=1
    
for t in q:
    ascii_value=ord(t)
    index=ascii_value-97
    print(hash_list[index])
