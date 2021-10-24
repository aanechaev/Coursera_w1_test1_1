n = int(input())
dig1 = n % 10
dig2 = (n % 100 - dig1) // 10
dig3 = (n - (n % 100)) // 100
print(dig1 + dig2 + dig3)
