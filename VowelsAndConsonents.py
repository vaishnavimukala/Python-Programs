s=input()
vowels=['a','e','i','o','u']
v=0
for i in s:
    if i in vowels:
        v+=1
print("Vowels in",s,"are",v)
print('Consonents in',s,'are',len(s)-v)
        
