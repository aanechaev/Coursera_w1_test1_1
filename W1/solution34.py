a = int(input())
b = int(input())
ar = ['YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO']
d1 = a // b
d2 = b // a
b1 = bool(d1)
b2 = bool(d2)
db1 = int(b1)
db2 = int(b2)
ar[db1] = str(a)
ar[db2] = str(b)
print(ar[1])
