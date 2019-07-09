A=int(input())55
M=list(map(int,input().split()))
for i in range(0,A-2):
 for j in range(i+1,A-1):
  for k in range(j+1,A):
   if(M[i]+M[j]==M[k]):
    print(M[i], M[j], M[k])
