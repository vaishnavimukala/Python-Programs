arr=list(map(int,input().split()))
turn=int(input())
for i in range(turn):
    temp=arr[0]
    arr.remove(temp)
    arr.append(temp)
print(arr)    
