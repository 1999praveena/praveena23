p=input()
m=set(map(int,input().split()))
a=set(map(int,input().split()))
if a.issubset(m):
  print("YES")
else:
  print("NO")
  
