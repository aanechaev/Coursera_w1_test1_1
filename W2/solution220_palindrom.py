n = int(input())
s = 1
dsu = 0
while s < n:
    d = []
    r = []
    m = s
    while m > 0:
        d.append(m % 10)
        m = m // 10
    r = d
    r.reverse()
    print(d)
    print(r)
    if r == d:
        dsu = dsu + 1
    s = s + 1
print(dsu)
