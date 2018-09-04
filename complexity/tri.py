def eclater(t):
    t1=[]
    t2=[]

    def charget1(i, t):
        t1.append(t[i])
        if i < len(t) - 1 and t[i + 1] > t[i]:
            charget1(i + 1, t)
        if i < len(t) - 1 and t[i + 1] < t[i]:
            charget2(i + 1, t)

    def charget2(i, t):
        t2.append(t[i])
        if i < len(t) - 1 and t[i + 1] > t[i]:
            charget2(i + 1, t)
        if i < len(t) - 1 and t[i + 1] < t[i]:
            charget1(i + 1, t)

    charget1(0,t)
    return t1,t2

def fusion(t1,t2):
    i,j=0,0;
    t=[]
    while (i<len(t1) and j<len(t2)):
        if t1[i]<t2[j] :
            t.append(t1[i])
            i+=1
        else:
            t.append(t2[j])
            j+=1
    if i>=len(t1):
        for k in range(j,len(t2)):
            t.append(t2[k])
    else:
        for k in range(i,len(t1)):
            t.append(t1[k])
    return t


def tri(t):
    l1=[]
    l2=[]
    while(True):
        l1,l2=eclater(t)
        t=fusion(l1,l2)
        if (len(l1)==0):
            return l2
        if (len(l2)==0):
            return l1
    return t








t=[10,5,3,8,14]
t=tri(t)
print(t)

