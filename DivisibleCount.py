N,D=map(int,input().split())
count=0
while N!=0:
    if N%D==0:
         count+=1
         N=int(N/4)
    else:
         break
print(count)        
