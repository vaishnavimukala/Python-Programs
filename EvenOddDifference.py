arr=list(map(int,input().split()))
e=0
o=0
for i in range(len(arr)):
    if i%2==0:
        e+=arr[i]
    else:
        o+=arr[i]
print(abs(e-o))        
