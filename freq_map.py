# m-1
valr=[1,1,4,5,2,2,8,9,0,0]
freq_dict={}
for i in range(len(valr)):
    if valr[i] in freq_dict:
        freq_dict[valr[i]]+=1
    
    else:
        freq_dict[valr[i]]=1
print(freq_dict.keys())
print(freq_dict[1])
