# В первой строке содержится целое число N (1 <= N <= 10^9).
# Последовательность чисел Фибоначчи задается следующим образом:
# F[1] = 1. F[2] = 1. F[k] = F[k - 1] + F[k - 2] для k >= 3.
# Определить, является ли N числом Фибоначчи.
# Если является, то вывести "True", если нет – вывести "False".

N = int(input())
prev = 1
cur = 1

while N <= cur:
    prev = cur - prev
    cur = cur + prev

if cur == N:
    print('True')
else:
    print('False')

