#Напишите программу, которая по заданному натуральному n печатает рисунок (см. ниже).
# В первой строке содержится n – количество строк. (1 <= n <= 20). Вывести рисунок.


n = int(input())
x = 0

for i in range(n):
    if i <= i * n:
        i = 3 * (x + 1)
        i = '*'
        x += 1
    for j in range(n):
        if j <= j * n:
        j = 3 * (x + 1) / 2
        j = '/'
        x += 1
print()
