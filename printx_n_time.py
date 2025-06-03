# print x , n times
x=15
n=3
def rt(x,n):
    if(n==0):
        return
    else:
        print(x)
        rt(x,n-1)
rt(x,n)
