str=input()
l=[i for i in str]
k=''
for i in l:
    if i not in k:
        k=k+i
print(k)        
       
