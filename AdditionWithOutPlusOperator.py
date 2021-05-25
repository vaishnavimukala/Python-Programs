n,m=map(int,input().split())
if n&m==0:
    print(n^m)
else:
    while m!=0:
        c=n&m
        n=n^m
        m=c<<1
    print(n)    
