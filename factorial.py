N=10
def fact(N):
  if(N==0 or N==1):
    return N
  return N*fact(N-1)
  
print(fact(N))
  

