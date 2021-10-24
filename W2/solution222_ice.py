a = int(input())
if (
    (a % 5 == 0) or
    (a % 3 == 0) or
    (a % 8 == 3) or
    (a % 8 == 6) or
    (a % 8 == 5) or
    (a % 8 == 0) or
    (a % 11 == 0) or
    (a % 11 == 3) or
    (a % 11 == 6) or
    (a % 11 == 5) or
    (a % 11 == 10) or
    (a % 13 == 0) or
    (a % 13 == 3) or
    (a % 13 == 6) or
    (a % 13 == 9) or
    (a % 13 == 12) or
    (a % 13 == 5) or
    (a % 13 == 10)
):
    print('YES')
else:
    print('NO')
