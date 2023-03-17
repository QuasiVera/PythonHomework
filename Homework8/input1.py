
def Input(data, number):

    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(f'{data} : {number} \n')
    print('Добавлено')
       