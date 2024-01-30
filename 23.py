# def f(x, h):
#     if h == 5:
#         a.add(x)
#     else:
#         f(x + 1, h + 1)
#         f(x * 2, h + 1)
#
#
# a = set()
# f(1, 0)
# print(a)
#
#
# def f(x, y):
#    if x > y:
#        return 0
#    if x == y:
#        return 1
#    else:
#        return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)
# print(f(4, 11) * f(11, 13))

# s = open('24.txt').read().strip()
# s = s.replace('A', '*')
# s = s.replace('B', '*')
# s = s.replace('C', '*')
# maxi = 1
# count = 1
# for i in range(1, len(s)):
#     if s[i-1]+s[i] != '**':
#         count += 1
#         maxi = max(maxi, count)
#     else:
#         count = 1
# print(maxi)

f = open('zadanie24_1.txt').readline()
k = m = 0
for i in range(len(f)):
    if (f[i] == 'A' and k%2 == 0) or (f[i] == 'B' and k%2 == 1):
        k += 1
        m = max(m, k)
    elif f[i] == 'A': k = 1
    else: k = 0
print(m)