'''
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход 
подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12
'''

enLetters1 = {'a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r', 'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'}
enLetters2 = {'d', 'g', 'д', 'к', 'л', 'м', 'п', 'у'}
enLetters3 = {'b', 'c', 'm', 'p', 'б', 'г', 'ё', 'ь', 'я'}
enLetters4 = {'f', 'h', 'v', 'w', 'y', 'й', 'ы'}
enLetters5 = {'k', 'ж', 'з', 'х', 'ц', 'ч'}
enLetters8 = {'j', 'x', 'ш', 'э', 'ю'}
enLetters10 = {'q', 'z', 'ф', 'щ', 'ъ'}

dictEn = {'8' : enLetters8, '10' : enLetters10, '1': enLetters1, '2': enLetters2, 
          '3' : enLetters3, '4': enLetters4, '5': enLetters5}

str = input('Введите слово: ')
str = str.lower()
score = 0
for k in range(0, len(str)): # идем по строке, перебираем по одной букве
    for i in dictEn:         # идем по словарю по ключам i
        for j in dictEn[i]:  # идем по значениям, j - это одна буква в множестве под ключом i
            if str[k] == j:
                i = int(i)
                print(f'{str[k]} -> {i}')
                #print(type(i))
                score = score + i
print(f'{str} -> {score} очков')
