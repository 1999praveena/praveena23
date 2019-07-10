pn=int(input())
qv=[int(x) for x in input().split()]
r=[]
for i in range(0,len(qv)):
        y=qv[i:]
        z=max(y)
        if qv[i]==z:
                r.append(qv[i])
print(*r)
print(max(qv))


