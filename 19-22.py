def f(s1,s2,hod):
    if ((hod ==3 or hod ==1 )and s1+s2 >=61) or hod>4:
        return False

    if((hod ==2 )and s1+s2 >=61):
        return True

    hod +=1

    mx = max(s1,s2)
    mi = min(s1,s2)

    if hod%2 == 0:
        return f(mx,mi+1,hod) or f(mi+2, mx,hod) or f(mx,mi*2,hod) #peter
    else:
        return f(mi+1, mx,hod) and f(mi+2, mx,hod) and f(mx,mi*2,hod)  #ivan


for s in range(1,67):
    if f(8,s,0):
        print(s)


