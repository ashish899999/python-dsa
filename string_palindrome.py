str="ashsa"
# check string is palidrome or not
i,j=0,len(str)-1
def pld(str,i,j):
    if(i>=j):
        print("palindrome")
        return
    if(str[i]!=str[j]):
        print("not a palidrome")
        return
    pld(str,i+1,j-1)
pld(str,i,j)
