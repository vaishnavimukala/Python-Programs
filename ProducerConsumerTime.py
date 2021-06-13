N=int(input())
P=list(map(int,input().split()))
C=list(map(int,input().split()))
time=P[0]+C[N-1]
p=0
c=0
for i in range(N):
    p+=P[i]
    c+=C[i]
p-=P[0]
c-=C[N-1]
if p>c:
    time+=p
else:
    time+=c
print(time)    
