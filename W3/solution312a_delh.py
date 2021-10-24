stroka = input()
srez = stroka[::-1]
a = stroka.find('h')
srez1 = stroka[:a]
b = srez.find('h')
srez2 = srez[:b]
srez3 = srez2[::-1]
print(srez1, end='')
print(srez3)
