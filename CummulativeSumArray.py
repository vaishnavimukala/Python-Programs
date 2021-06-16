arr=list(map(int,input().split()))
l=[]
l.append(arr[0])
for i in range(1,len(arr)):
    k=l[i-1]+arr[i]
    l.append(k)
print(l)    
