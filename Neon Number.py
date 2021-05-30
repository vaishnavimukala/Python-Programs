n=int(input())
m=n**2
s=0
while m!=0:
    r=m%10
    s+=r
    m=m//10
if s==n:
    print(n,"Neon Number")
else:
    print(n,'not a Neon Number')
