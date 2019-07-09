P=int(input())
M=list(map(int,input().split()))
for i in range(0,P-2):
 for j in range(i+1,P-1):
  for k in range(j+1,P):
   if(M[i]+M[j]==M[k]):
    print(M[i], M[j], M[k])
