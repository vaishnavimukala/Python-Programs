n,m=map(int,input().split())
sn=0
sm=0
for i in range(1,n+1):
    if n%i==0:
        sn=sn+i
for i in range(1,m+1):
    if m%i==0:
        sm=sm+i
#print(sn,sm)
if sn/n==sm/m:
    print(n,m,' are Friendly Pairs')
else:
    print(n,m,' are not Friendly Pairs')
