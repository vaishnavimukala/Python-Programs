no_A=int(input())
A=set(map(int,input().split()))
no_others=int(input())
for _ in range(no_others):
    op,num=input().split()
    if op=='intersection_update':
            A=A&set(map(int,input().split()))
    elif op=='update':                   
            A=A|set(map(int,input().split()))
    elif op=='symmetric_difference_update':
            A= A^set(map(int,input().split()))
    else:                   
            A=A-set(map(int,input().split()))
        
print(A))       
