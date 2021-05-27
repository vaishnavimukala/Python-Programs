n=list(map(int,input().split()))
l=[]
for i in range(0,len(n),2):
    for j in range(n[i]):
        l.append(n[i+1])
print(l)
