n = int(input())
nf = float(n)
sm = 0.0
i = 1
while i <= n:
    sm = sm + (1 / (i ** 2))
    i = i + 1
print(sm)
