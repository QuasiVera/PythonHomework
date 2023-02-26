'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
    N = 5
    1 2 3 4 5
    X = 6
    -> 5
'''
from math import fabs
N = int(input('Введите размер массива N: '))
list = []
for i in range(0, N):
    i = int(input(f'Введите элемент массива {i}: '))
    list.append(i)
x = int(input('Введите x: '))

min = 147483648
iMin = 0
for i in range(0, len(list)):
    temp = abs(list[i]-x)
    if temp < min:
        min = temp
        iMin = i
print(list)        
print(f' ближе всего к {x}: {list[iMin]}')

