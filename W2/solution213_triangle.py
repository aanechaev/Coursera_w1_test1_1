a = int(input())
b = int(input())
c = int(input())


def tritype(m, n, k):
    if m**2 == n**2 + k**2:
        print('rectangular')
    elif m**2 < n**2 + k**2 and m < n + k:
        print('acute')
    elif m**2 > n**2 + k**2 and m < n + k:
        print('obtuse')
    elif m >= n + k:
        print('impossible')
    return 0


if a > b and a > c:
    tritype(a, b, c)
elif b > a and b > c:
    tritype(b, a, c)
elif c > b and c > a:
    tritype(c, b, a)
else:
    tritype(a, b, c)
