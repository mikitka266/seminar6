#Таблица умножения, сложения и возведения в степень
#print_operation_table(operation, num_rows=9, num_columns=9)
num_rows=int(input('Введите число строк '))
num_colums =int(input('Ввдеите число столбцов '))
mult=[x*y for x in range(1,num_rows+1) for y in range(1,num_colums+1)]
addition = [x+y for x in range(1,num_rows+1) for y in range(1,num_colums+1)]
exponent = [x**y for x in range(1,num_rows+1) for y in range(1,num_colums+1)]
data = list(zip(mult,addition,exponent))
print(*data, end = '\t')
