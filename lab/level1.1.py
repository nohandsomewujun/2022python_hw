# level1.1 code
# y = x^2 - 2*x + 1

from math import sqrt


def solve(y):
    res = []
    # special case
    if y < 0:
        return res
    if y == 0:
        res.append(1)
        return res
    # normal case
    a = sqrt(y)
    res.append(a+1)
    res.append(-a+1)
    return res


y = int(input("y:"))
res = []
res = solve(y)
if res == []:
    print("error input")
else:
    for i in res:
        print(i)
