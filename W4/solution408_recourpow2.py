def power(a, n):
    if n > 0:
        n = n - 2
        sum = (a ** 2) * power(a, n)
    else:
        sum = 1
    return sum


a1 = float(input())
n1 = int(input())
if n1 == 0:
    print("1")
elif n1 == 1:
    print(a1)
elif n1 % 2 == 0:
    print(power(a1, n1))
else:
    print(power(a1, n1 - 1) * a1)
