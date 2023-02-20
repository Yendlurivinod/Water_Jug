def fill(j,c,c1):
    if c1!=0:
        j=j+c1
        if j<=c:
            return j,0
        else:
            return c,(j-c)
    else:
        j=c
        return j
def empty(l):
    return 0


l=[0,0]
c=list(map(int,input().split())) # read capacities of jugs
rs=int(input())    # required amount of water
if c[0]%2==0 and c[1]%2==0 and rs%2==1:
    print('NO SOLUTION')
else:
    while(1):
        if l[0]==0 and l[1]==0:
            l[0]=fill(l[0],c[0],0)
            print(l)
            if l[0]==rs or l[1]==rs:
                break
        elif l[0]!=0 and l[1]==0:
            l[1],l[0]=fill(l[1],c[1],l[0])
            print(l)
            if l[0]==rs or l[1]==rs:
                break
        elif l[0]!=0 and l[1]==c[1]:
            l[1]=empty(l[1])
            print(l)
            if l[0]==rs or l[1]==rs:
                break
        elif l[0]!=0 and l[1]!=0:
            l[1],l[0]=fill(l[1],c[1],l[0])
            print(l)
            if l[0]==rs or l[1]==rs:
                break
        elif l[0]==0 and l[1]!=0:
            l[0]=fill(l[0],c[0],0)
            print(l)
            if l[0]==rs or l[1]==rs:
                break
        elif l[0]==c[0] and l[1]==c[1]:
            l[1]=empty(l[1])
            print(l)
            if l[0]==rs or l[1]==rs:
                break
