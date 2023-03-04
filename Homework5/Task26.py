'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''

#======================== Возведение в степень рекурсией =================

def Pow(a,b):
    if b==0: return 1
    if b==1: return a
    else:
        return Pow(a,b-1)*a

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
b = GetUserNumber('Введите степень B: ')
print(f' {a}^{b} = {Pow(a,b)}')