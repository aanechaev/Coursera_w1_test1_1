stroka = input()
a = stroka.find(' ')
srez1 = stroka[:a]
srez2 = stroka[a + 1:]
print(srez2, srez1)
