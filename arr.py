a,m=map(int,input().split())
p=[]
for i in range(a):
  s=set(map(int,input().split()))
  p.append(s)
n=s.intersection(*p)
print(*n)
