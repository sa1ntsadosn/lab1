print('Введите четырёх значное число:')
a = int(input())
b = a
a = b%10
b = (b*0.1)//1
c = b%10
b = (b*0.1)//1
d = b%10
b = (b*0.1)//1
f = b%10
print('Произведение цифр числа', a*c*d*f)