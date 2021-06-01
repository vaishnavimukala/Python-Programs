def SubArrays(l):
     k=[[]]
     for i in range(0,len(l)+1):
          for j in range(i):
               p=l[j:i]
               k.append(p)
     for i in range(1,len(l)-1):
          o=[]
          o.append(l[i-1])
          o.append(l[i+1])
          k.append(o)
     k.append(l[::len(l)-1])    
     return k
l=list(map(int,input().split()))
n=int(input())
res=SubArrays(l)
#print(res) All the subarrays
f=[]
for i in res:
    if len(i)==n:#Subarrays of size n
         f.append(i)
print(max(f))  # subarrays of n size with max sum  
        

        
