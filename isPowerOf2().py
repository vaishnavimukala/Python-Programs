def power2(num):
    f=False
    while num>1:
          if num%2==0:
              f=True
          else:
              f=False
              break
          num=int(num/2)
    return f
n=int(input())
print(power2(n))
