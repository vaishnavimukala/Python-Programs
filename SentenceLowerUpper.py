s=input()
#print(len(s))
c1=0
c2=0
for i in s:
    if i.islower()==True:
        c1+=1
print('Lower case letters',c1)        
for i in s:
    if i==" ":
        c2+=1
#print('No of spaces',c2)
print('Upper case letters:',(len(s)-(c1+c2)))
