n=int(input())#25 5  6  376
m=n*n#625  25  36  76
l=len(str(n))
temp=(m//(10**l))*(10**l)
if m-temp==n:
    print(n,'Automorphic Number')
else:
    print(n,'Not a Automorphic Number')
