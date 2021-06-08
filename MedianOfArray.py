arr=list(map(int,input().split()))
arr.sort()
k=len(arr)//2
if len(arr)%2==0:
    print((arr[k-1]+arr[k])/2)
else:
    print(arr[k])

