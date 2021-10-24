def MinDivisor(n):
    a = 2
    while n % a != 0:
        a += 1
        if a > (n ** 0.5) + 1:
            return 'YES'
    if n == 2:
        return 'YES'
    return 'NO'


n1 = int(input())
print(MinDivisor(n1))
