ap=int(input())
s=0
while(ap>0):
  a=ap%10
  s=s+a
  ap//=10
print(s)
