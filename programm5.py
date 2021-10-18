import math

print('Введите значение катета a:')
a = int(input())
print('Введите значение катета b:')
b = int(input())
c = math.sqrt(a*a+b*b)
P = a+b+c
S = (a*b)/2
print('Периметр треугольник:', P)
print('Площадь треугольника:', S)
exit(1)