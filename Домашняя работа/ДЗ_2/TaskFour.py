'''
Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите,
может ли слон попасть с первой клетки на вторую одним ходом. Формат входных данных:
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Формат выходных данных: Программа должна вывести YES, если из первой клетки ходом слона
можно попасть во вторую или NO в противном случае.'''

FirstEleph_X = int(input())
FirstEleph_Y = int(input())
SecondEleph_X = int(input())
SecondEleph_Y = int(input())

if SecondEleph_X == FirstEleph_X - 1 and SecondEleph_Y == FirstEleph_Y - 1 or SecondEleph_X == FirstEleph_X - 1 and SecondEleph_Y == FirstEleph_Y + 1:
    print('Yes')
elif SecondEleph_X == FirstEleph_X + 1 and SecondEleph_Y == FirstEleph_Y - 1 or SecondEleph_X == FirstEleph_X + 1 and SecondEleph_Y == FirstEleph_Y + 1:
    print('Yes')
else:
    print('No')

