p=int(input(""))
na=list(map(int,input().split()))
o=len(na)
l=max(na)
y,z=0,0
for i in range(0,o-1):
 for j in range(i+1,o):
  if abs(na[i]+na[j])< l:
   y,z=na[i],na[j]
   l=abs(y+z)
print(y, z)
