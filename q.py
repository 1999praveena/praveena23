import math
p,v=map(int,input().split())
m=list(map(int,input().split()))[:p]
l=[]
for i in range (0,v):
    l,r=map(int,input().split())
    l.append([l,r])
for i in l:
    le=i[0]-1
    ri=i[1]-1
    print(math.gcd(m[le],m[ri]))
