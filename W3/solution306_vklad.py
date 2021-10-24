p = int(input())
x = int(input())
y = int(input())
sm = (float(x) + (y / 100)) * ((p / 100) + 1.0)
nc = int(sm)
ns = (sm - float(nc))
ns1 = ns * 100
ns2 = int(ns1)
if abs(ns1 - ns2) > 0.999999:
    ns2 = ns2 + 1
print(nc, ns2)
