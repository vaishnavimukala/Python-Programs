def facto(x):
    if x<=1:
        return 1
    else:
        return x*facto(x-1)
n=int(input())
m=str(n)
s=0
for i in m:
    s=s+facto(int(i))
if s==n:
    print(n,'Strong Number')
else:
    print(n,'not a Strong Number')
