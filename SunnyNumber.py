import math
n=int(input())
k=math.sqrt(n+1)
#print(k)
p=int(k)
#print(p)
#print(k-p)
if k-p==0:
    print(n,'is Sunny Number')
else:
    print(n,'is not a Sunny Number')
