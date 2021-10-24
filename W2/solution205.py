X1 = int(input())
Y1 = int(input())
X2 = int(input())
Y2 = int(input())
movX = abs(X2 - X1)
movY = abs(Y2 - Y1)
if (movX <= 1) and (movY <= 1):
    print('YES')
else:
    print('NO')
