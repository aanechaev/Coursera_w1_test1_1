stroka = input()
srez = stroka[::-1]
srez2 = ''
if (stroka.find('f')) != -1:
    print(stroka.find('f'), end=' ')
    srez2 = stroka[stroka.find('f') + 1:]
if (srez2.find('f')) != -1:
    print((len(srez) - srez.find('f') - 1), end=' ')
