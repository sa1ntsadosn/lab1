import math

print('Введите x:')
x = float(input())
print('Введите y (y!=pi/4 + pi*n/2):')
y = float(input())
print('Введите z:')
z = float(input())
a: float = (2 * (math.cos(x - (math.pi/6))))/((1/2)+math.pow(math.sin(y), 2))
b: float = 1 + math.pow(z, 2)/(3+(math.pow(z, 2)/5))
print('Результат вычисления a: ', a)
print('Результат вычисления b: ', b)