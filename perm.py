from itertools import permutations
p=list(input())
s = permutations(p)
for i in list(s):
    print(*i,sep="")
