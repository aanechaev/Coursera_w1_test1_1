def sommaire(a, b):
    if b > 1:
        b = b - 1
        sum2 = sommaire(a, b) + 1
    else:
        sum2 = a + 1
    return sum2


a1 = int(input())
b1 = int(input())
if b1 == 0:
    print(a1)
else:
    print(sommaire(a1, b1))
