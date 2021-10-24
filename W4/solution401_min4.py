def IsPointInSquare(x, y):
    return (x <= 1.0) and (x >= -1.0) and (y >= -1.0) and (y <= 1.0)


x1 = float(input())
y1 = float(input())
if IsPointInSquare(x1, y1):
    print('YES')
else:
    print('NO')
