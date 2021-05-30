n=int(input())
m=n
sum=0
i=len(str(n))
while m!=0:
    d=m%10
    sum=sum+d**i
    m=m//10
    i-=1
if n==sum:
    print(n,'Disarium Number')
else:
    print(n,'not a Disarium Number')
