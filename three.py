p,l=map(int,input().split())
am=list(map(int,input().split()))
a=[]
for i in am:
    a.append([abs(i-l)]+[i])
a.sort()
a.pop(0)
for i in a[:3]:
    print(i[1],end=' ')
