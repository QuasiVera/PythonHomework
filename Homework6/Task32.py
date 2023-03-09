'''
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного максимума)

Ввод массива
Ввод мин и макс значений
Вывод индексов элементов между мин и макс
'''

#import random
#n = int(input('n = '))
#array = [random.randrange(0, 30) for i in range(n+1)]
array = [int(i) for i in input('Введите элементы массива: ').split()]
print(array)
min = int(input('Введите минимум: '))
max = int(input('Введите максимум: '))


for i in range(len(array)):
    if array[i]>=min and array[i]<=max:
        print(i, end=' ')
