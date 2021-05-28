n=int(input())
def palin(x):
    s=str(x)
    if s==s[::-1]:
        return True
    else:
        return False
small=n-1
while (not palin(small)):
    small=small-1
larg=n+1
while (not palin(larg)):
    larg=larg+1
d1=abs(small-n)
d2=abs(larg-n)
if d1<d2 and d1!=0 and d2!=0:
    print(small)
else:
    print(larg)
    
    
    
        
        

        
