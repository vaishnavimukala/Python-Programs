#n=901 9+0+1=10 1+0=1 sum recursively =1
n=int(input())
s=1
l=[int(x) for x in str(n)]
while len(l)!=1:
    s=sum(l)
    #print(s)
    l=[int(x) for x in str(s)]
    #print(l)
if s==1:
    print(n,'Magic Number')
else:
    print(n,'Not a Magic Number')
