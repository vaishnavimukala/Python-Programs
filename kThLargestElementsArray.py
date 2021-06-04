n=list(map(int,input().split()))
k=int(input())
temp=n
while (k-1)!=0:
    y=max(temp)
    temp.remove(y)
    k=k-1
print(max(temp))

