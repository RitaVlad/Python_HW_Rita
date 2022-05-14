'''
Покупка пирожков
Пирожок в столовой стоит А рублей и B копеек. Определите, сколько рублей и копеек нужно заплатить за N пирожков.

Формат входных данных
Программа получает на вход три числа: A, B, N - целые, положительные, не превышают 10000.

Формат выходных данных
Программа должна вывести два числа через пробел: стоимость покупки в рублях и копейках.
'''

num = int(input('Введите количество пирожков: '))
PriceOne = int(input('Введите количество рублей за 1 пирожок: '))
PricePenny = int(input('Введите количество копеек а 1 пирожок: '))
PriceAll = num * PriceOne

if PricePenny // 100 > 1:
    Value = PriceAll + PricePenny // 100
    PricePenny = PricePenny % 100
else:
    Value = PriceAll
    PricePenny = PricePenny

answer = str(Value) + ' руб.' + str(PricePenny) + ' коп.'
print(answer)

