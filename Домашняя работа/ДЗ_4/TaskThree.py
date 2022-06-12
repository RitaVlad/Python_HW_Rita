# Даны два целых числа a и b. Найти сумму квадратов чисел от a до b включительно.
a = int(input())
b= int(input())
summ = 0


for i in range(a, b + 1):
    i = i ** 2
    summ += int(i)
    print(summ)
