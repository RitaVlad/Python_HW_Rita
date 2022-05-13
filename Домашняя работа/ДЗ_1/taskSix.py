'''
Разность времен
Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды
для каждого из моментов времени. Известно, что второй момент времени наступил не раньше первого.
Определите, сколько секунд прошло между двумя моментами времени.

Формат входных данных
Программа на вход получает три целых числа: часы, минуты, секунды, задающие первый момент времени и
три целых числа, задающих второй момент времени.

Формат выходных данных
Выведите число секунд между этими моментами времени.
'''
# Найдем время первого момента в секундах
Firsthours = int(input())
Firstminutes = int(input())
Firstseconds = int(input())
hours = Firsthours * 3600
minutes = Firstminutes * 60
FirstTime = hours + minutes + Firstseconds

#Найдем время второго момента в секундах
SecondHours = int(input())
SecondMinutes = int(input())
SecondSeconds = int(input())
hours = SecondHours * 3600
minutes = SecondMinutes * 60
SecondTime = hours + minutes + SecondSeconds

# Найдем разницу в секундах между моментом первого и второго момента
Delta = SecondTime - FirstTime
print(Delta)



