n=input()
dic=dict()
for i in set(n):
    dic[i]=n.count(i)
for i in dic:
    if dic.get(i)==max(dic.values()):
        print(i,':',max(dic.values()))

