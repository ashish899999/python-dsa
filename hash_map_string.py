s="aaaabbcfdss"
q=["a","s"]
hash_map={}
for i in range(len(s)):
    hash_map[s[i]]=hash_map.get(s[i],0)+1
for char in q:
    print(hash_map.get(char,0))
