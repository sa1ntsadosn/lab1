print('Введите a1:')
a1 = float(input())
print('Введите b1:')
b1 = float(input())
print('Введите c1:')
c1 = float(input())
print('Введите a2:')
a2 = float(input())
print('Введите b2:')
b2 = float(input())
print('Введите c2:')
c2 = float(input())
print('Введите a3:')
a3 = float(input())
print('Введите b3:')
b3 = float(input())
print('Введите c3:')
c3 = float(input())
print('Введите d1:')
d1 = float(input())
print('Введите d2:')
d2 = float(input())
print('Введите d3:')
d3 = float(input())
op = float(a1*b2*c3+b3*a2*c1+a3*c2*b1-a3*b2*c1-a2*b1*c3-a1*c2*b3)
if op == 0:
 print('Определитель равен 0, решения далее нет.')
else:
    op_a = float(d1*b2*c3+d3*b1*c2+d2*c1*b3-d3*b2*c1-d2*b1*c3-d1*b3*c2)
    op_b = float(a1*d2*c3+a3*d1*c2+a2*d3*c1-a3*d2*c1-a2*d1*c3-a1*c2*d3)
    op_c = float(a1*b2*d3+a3*b1*d2+a2*b3*d1-a3*b2*d1-a2*b1*d3-a1*d2*b3)
    x = float(op_a/op)
    y = float(op_b/op)
    z = float(op_c/op)
    print('Значение x:', x)
    print('Значение y:', y)
    print('Значение y:', z)