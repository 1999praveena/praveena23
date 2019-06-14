p=input()
b=0
a=0
for j in p:
    if(j.isalpha()==True):
        a=a+1
    elif(j.isdigit()==True):
        b=b+1
if(a>0 and b>0):
    print("Yes")
else:
    print("No")
