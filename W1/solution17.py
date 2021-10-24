n = int(input())
dig1 = n % 60
dig2 = (n % 1440 - dig1) // 60
print(dig2, dig1)
