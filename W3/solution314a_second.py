stroka = input()
srez2 = ''
a = stroka.find('f')
if a != -1:
    srez2 = stroka[stroka.find('f') + 1:]
    if (srez2.find('f')) != -1:
        print(srez2.find('f') + a + 1)
    else:
        print('-1')
else:
    print('-2')
