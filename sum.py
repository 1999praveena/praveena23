am=int(input())
if am<=100000:
  c=0
  for i in range(0,am):
    c=c+am
    am=am-1
  print(c)
