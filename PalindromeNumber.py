n=int(input())
m=n
s=''
while m!=0:
    d=m%10
    s=s+str(d)
    m=m//10
if n==int(s):
    print(n,'is Palindrome Number')
else:
    print(n,'is not a Palindrome Number')

    
