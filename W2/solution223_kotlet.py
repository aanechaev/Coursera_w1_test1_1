k = int(input())
m = int(input())
n = int(input())
pr = (n // k)
if (n % k) != 0 and (n % k <= k // 2) and n > k:
    pr2 = (pr * 2) + 1
elif (n % k) != 0:
    pr2 = (pr * 2) + 2
elif (n % k) == 0:
    pr2 = pr * 2
print(pr2 * m)
