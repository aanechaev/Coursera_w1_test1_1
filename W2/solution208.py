n = int(input())
m = int(input())
k = int(input())
if(
    ((k % n == 0) and (k <= (m * n - n))) or
    ((k % m == 0) and (k <= (m * n - m)))
):
    print('YES')
else:
    print('NO')
