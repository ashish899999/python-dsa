s="aaaabccdd"
q=["a","c"]
for char  in q:
    count=0
    for char2 in s:
        if(char==char2):
            count+=1
    print(count)
