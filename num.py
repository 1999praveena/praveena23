p,a=map(int,input().split())
l=list(map(int,input().split()))[:p]
l.sort(reverse=True)
print(l[a-1])
