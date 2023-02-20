'''
Задача 4: Требуется определить, можно ли от шоколадки размером n x m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
'''

n = int(input('Введите размер шоколадки n: '))
m = int(input('Введите размер шоколадки m: '))
k = int(input('Введите нужное число долек k: '))
res = ''
if (k%n == 0 or k%m == 0) and k<n*m:
    res = 'yes'
else:
    res = 'no'
print(f'{n} {m} {k} -> {res}')

