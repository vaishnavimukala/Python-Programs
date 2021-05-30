x=int(input())
y=int(input())
l=[]
k=[]
for i in range(1,(x//2)+1):
    if x%i==0:
        l.append(i)
for i in range(1,(y//2)+1):
    if y%i==0:
        k.append(i)
if sum(l)==y and sum(k)==x:
    print("Amicable Numbers")
else:
    print("Not Amicable Numbers")
