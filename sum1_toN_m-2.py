N=10
def prt(N):
    if(N==1):
        return 1
    return N+ prt(N-1)
print(prt(N))
