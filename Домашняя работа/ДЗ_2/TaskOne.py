#Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
#Формат входных данных: Вводятся 3 целых числа


FirstNum = int(input('Введите первое число: '))
SecondNum = int(input('Введите второе число: '))
ThirdNum = int(input('Введите третье число: '))

if FirstNum == SecondNum and SecondNum == ThirdNum:
    print('3')
elif FirstNum == SecondNum or FirstNum == ThirdNum:
    print('2')
else:
    print('0')
