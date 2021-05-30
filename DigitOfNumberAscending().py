N=int(input())
t=[int(x) for x in str(N)]
flag = 0
i = 1
while i < len(t):
      if(t[i]<t[i - 1]):
            flag = 1
      i += 1
if (not flag) :
      print ("YES")
else :
      print ("NO")
