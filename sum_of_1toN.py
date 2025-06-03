# sum of 1 to N
N=10
current_sum=0
def ptsum(N,current_sum):
    if(N==0):
        return current_sum
    return ptsum(N-1,current_sum+N)
print(ptsum(N,0))
