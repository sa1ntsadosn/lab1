print('Введите трехзначное число:')
a = int(input())
b = a/10
b = b%1*10//1
c = a//10
c = c%10
d = a//100
print(b, c, d)
