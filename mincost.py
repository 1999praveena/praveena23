p,o=input().split()
d=abs(len(o)-len(p))
for i in range(len(p)):
    if(len(o)==1 and o[i] in p):
        break
    if (p[i]!=o[i]):
        d=d+1
print(d)
