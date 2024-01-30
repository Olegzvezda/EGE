def f(s1,s2,hod):
    if ((hod ==1 or hod ==3) and s1+s2 >=62) or hod >4:
        return False
    if (hod ==2 or hod == 4) and s1+s2 >=62:
        return True

    hod+=1

    if hod%2 == 0:
        return f(s1+1,s2, hod) or f(s1,s2+1, hod) or f(s1*2,s2, hod) or f(s1,s2*2, hod)
    else:

        return f(s1+1,s2, hod) and f(s1,s2+1, hod) and f(s1*2,s2, hod) and f(s1,s2*2, hod)

for s in range(1, 52):
    if f(10,s,0):
        print(s)