n=int(input())
s=0
m=1
t=n
while t!=0:
    d=t%10
    s+=d
    m*=d
    t=t//10
if s==m:
    print(n,'is Spy Number')
else:
    print(n,'is not a Spy Number')
