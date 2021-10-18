from tabulate import tabulate
print('Введите 1 наименование:')
name1 = str(input())
print('Введите 2 наименование:')
name2 = str(input())
print('Введите 3 наименование:')
name3 = str(input())

print('Введите тип 1: Б/З')
type1 = str(input())
print('Введите тип 2: Б/З')
type2 = str(input())
print('Введите тип 3: Б/З')
type3 = str(input())

print('Введите площадь посева(га)', name1)
s1 = str(input())
print('Введите площадь посева(га)', name2)
s2 = str(input())
print('Введите площадь посева(га)', name3)
s3 = str(input())

print('Введите уражайность(ц/га)', name1)
yr1 = str(input())
print('Введите уражайность(ц/га)', name2)
yr2 = str(input())
print('Введите уражайность(ц/га)', name3)
yr3 = str(input())

st = [['Селькохозяйственные культуры', '', '', ''],
       ['Наименование',  'Тип', 'Посевная площадь(га)', 'Урожайность (ц/га)'],
       [name1, type1, s1, yr1],
       [name2, type2, s2, yr2],
       [name3, type3, s3, yr3],
       ['Перичисляемый тип: З - зерновые, Б - бобовые']]
print(tabulate(st, tablefmt="grid"))