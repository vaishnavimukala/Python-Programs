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
x=list(map(int,input().split()))
s=int(input())
res=SubArrays(x)
for i in list(res):
    if sum(i)==s:
        print(i)


