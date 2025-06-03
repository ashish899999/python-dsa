num=[1,2,3,4,6,7,9,0]
# reverse the array using loops
i=0
j=len(num)-1
while(i<j):
    num[i],num[j]=num[j],num[i]
    i,j=i+1,j-1
print(num)
