p=int(input())
ib=1
while(ib<=p):
    v=0
    if(p%ib==0):
        j=1
        while(j<=ib):
            if(ib%j==0):
                v=v+1
            j=j+1
        if(v==2):
            print(ib,end=" ")
    ib=ib+1
