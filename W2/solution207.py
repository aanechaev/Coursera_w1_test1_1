X1 = int(input())
Y1 = int(input())
X2 = int(input())
Y2 = int(input())
if ((X1 % 2 == 0) and (Y1 % 2 == 0)) or ((X1 % 2 != 0) and (Y1 % 2 != 0)):
    black1 = True
    white1 = False
else:
    white1 = True
    black1 = False
if ((X2 % 2 == 0) and (Y2 % 2 == 0)) or ((X2 % 2 != 0) and (Y2 % 2 != 0)):
    black2 = True
    white2 = False
else:
    white2 = True
    black2 = False
if (black1 and black2) or (white1 and white2):
    print('YES')
else:
    print('NO')
   print('YES')
else:
    print('NO')
