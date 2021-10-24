def power(a, n):
    if n > 1:
        n = n - 1
        sum = a * power(a, n)
    else:
        sum = a
    return sum


a1 = float(input())
n1 = int(input())
if n1 == 0:
    print("1")
else:
    print(power(a1, n1))
