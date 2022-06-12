n = int(input())
k = 1
res = 0
summ = 0
for i in range(2, n + 1):
    k = k * i
    summ += 1/i
    res = k / summ
print('%.6f' % res)

