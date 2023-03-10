def print_operation_table(operation, num_rows=6, num_columns=6):

    a = [[0] * num_columns for i in range(num_rows)]

    for i in range(1, len(a)):              # не с 0 потому что нулевые столбец и строка будут все нулями,
        for j in range(1, len(a[i])):       # а в случае передачи через лямбду деления будет ошибка деления на ноль
            a[i][j] = operation(i,j)
            print(a[i][j], end=' ')
        print()
        
print_operation_table(lambda x, y: x+y)
print_operation_table(lambda x, y: x/y)

