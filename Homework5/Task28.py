'''
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4 
'''

#======================== Возведение в сепень рекурсией =================

def Sum(a,b):
    if b==0: return a
    if a==0: return b
    s = Sum(a,b-1)

    return s+1

#========================= Ввод данных ==================

def GetUserNumber(message_to_user):
    flag = True
    while flag:
        try:
            print(message_to_user)
            n = int(input())
            if n or n==0:
                flag = False
                return n
        except ValueError:
            print('Ошибка ввода! Введено не число')



#===============================

a = GetUserNumber('Введите число A: ')
b = GetUserNumber('Введите число B: ')
print(f' {a}+{b} = {Sum(a,b)}')