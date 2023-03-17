#data = input('Введите фамилию: ')
def Delete(data):
    data = data.lower()
    data_file = []
    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if data not in line.lower():
                data_file.append(line)
    
    str_data_file = ''.join(data_file)
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.write(str_data_file)
    print('Удалено')
    #return str_data_file

#print(Delete(data))

def Edit(data):
    data = data.lower()
    data_file = []
    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if data not in line.lower():
                data_file.append(line)
            else:
                temp = line.split(':')
                if data in temp[0].lower():
                    temp[0] = input('Введите новую фамилию и имя: ')
                elif data in temp[1].lower():
                    temp[1] = input('Введите новый номер телефона: ')
                data_file.append(f'{temp[0]} : {temp[1]}')
    
    str_data_file = ''.join(data_file)
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.write(str_data_file)
    print('Отредактировано')
                
    #return data_file
#print(Edit(data))

        
