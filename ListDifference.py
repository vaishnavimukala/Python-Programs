k=list(map(int,input().split()))
l=list(map(int,input().split()))
count=0
for i in range(len(k)):
    if l[i]!=k[i]:
        count+=1
print(count)        
        
