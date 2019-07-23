def Fi(a):
    from math import sqrt, trunc
    can_5 = sqrt(5)
    re = (1 / can_5) * ( ((1 + can_5)/2)**a - ((1 - can_5)/2)**a )
    from decimal import Decimal, getcontext
    getcontext().prec = len(str(trunc(re)))
    return int(Decimal(re)/1)

while 1:
    n = int(input('n = '))
    if n == 1 or n == 2:
        print('F(n) = 1')
    else:
        print('F(n) = ',Fi(n))

