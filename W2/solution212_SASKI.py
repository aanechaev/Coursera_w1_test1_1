x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
movx = x2 - x1
movy = y2 - y1
if (movy > 0) and (movx <= movy):
    if(
        (((x1 % 2 == 0) and (y1 % 2 == 0)) or
            ((x1 % 2 != 0) and (y1 % 2 != 0))) and
        (((x2 % 2 == 0) and (y2 % 2 == 0)) or
            ((x2 % 2 != 0) and (y2 % 2 != 0)))
    ):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
