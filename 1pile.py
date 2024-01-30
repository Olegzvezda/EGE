def f(s1,hod):
    if (hod == 1 or hod == 3) and s1 >=69:
        return False
    if hod>4:
        return False

    if (hod == 2 or hod ==4) and s1 >=69:
        return True


    # if hod >2:
    #     return False

    hod +=1

    if hod%2 != 0:
        return f(s1+1,hod) and f(s1+2,hod) and f(s1*2,hod) #peter
    else:
        return f(s1+1,hod) or f(s1+2,hod) or f(s1*2,hod)

for s in range(1,69):
    if f(s,0):
        print(s)


