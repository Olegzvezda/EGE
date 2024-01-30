#s = '0'+ '1' * 69 + '2' * 69 + '0'
def simple(a):
    for i in range(2, int(a ** (1 / 2))+1):
        if a % i == 0:
            return False
    return True


for i in range(70, 10000):
    s = '0' + '21' * i + '0'

    while '00' not in s:
        s = s.replace('02', '101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('12', '21', 1)
        s = s.replace('010', '00', 1)
    a = s.count('2')*2 + s.count('1')
    if simple(a):
        print(i)
        break


