def fact(n):
  if(n==0):
    return 1
  else:
    return(n*fact(n-1))
n=int(input("enter the value of n:"))
print("the Factorical of",n,"is:",fact(n))