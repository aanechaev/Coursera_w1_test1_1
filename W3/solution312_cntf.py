stroka = input()
srez = stroka[:]
sma = 0
while srez.find('f') != -1:
    a = srez.find('f')
    sma = sma + a
    print(sma, end=' ')
    srez = srez[(a + 1):]
    sma = sma + 1