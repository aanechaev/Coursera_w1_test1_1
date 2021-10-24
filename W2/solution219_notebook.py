def fln(box, side):
    qnt = 0
    qbx = 0
    while qbx <= (side - box):
        qbx = qbx + box
        qnt = qnt + 1
    return qnt


a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
sum = [0, 0, 0, 0, 0, 0]
max = 0
sum[0] = fln(a2, a1) * fln(b2, b1) * fln(c2, c1)
sum[1] = fln(a2, a1) * fln(c2, b1) * fln(b2, c1)
sum[2] = fln(b2, a1) * fln(a2, b1) * fln(c2, c1)
sum[3] = fln(b2, a1) * fln(c2, b1) * fln(a2, c1)
sum[4] = fln(c2, a1) * fln(b2, b1) * fln(a2, c1)
sum[5] = fln(c2, a1) * fln(a2, b1) * fln(b2, c1)
for a in sum:
    if a > max:
        max = a
print(max)
