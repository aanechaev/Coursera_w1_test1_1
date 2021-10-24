h = int(input())
d0 = h % 10
d1 = (h % 100) // 10
d2 = (h % 1000) // 100
d3 = h // 1000
if (d3 == d0) and (d2 == d1):
    print('1')
else:
    print('0')
