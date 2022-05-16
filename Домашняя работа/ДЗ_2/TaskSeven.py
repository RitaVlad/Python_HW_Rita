M = int(input())
N = int(input())
K = int(input())

# Найдем площадь прямоугольника
S = M * N
HalfPfChoc = S // 2
if HalfPfChoc == K:
    print('Yes')
else:
    print('No')



