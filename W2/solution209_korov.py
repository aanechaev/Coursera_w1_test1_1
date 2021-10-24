a = int(input())
if a > 20:
    if a % 10 == 1:
        print(a, 'korova')
    elif ((a % 10) >= 2) and ((a % 10) <= 4):
        print(a, 'korovy')
    else:
        print(a, 'korov')
if a <= 20:
    if a == 1:
        print(a, 'korova')
    elif (a >= 2) and (a <= 4):
        print(a, 'korovy')
    else:
        print(a, 'korov')
