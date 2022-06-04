N = int(input('Введите год: '))

if (N % 4 == 0) and (N % 100 != 0):
    print('Високосный')
elif (N % 400 == 0):
    print('Високосный')
else:
    print('Обычный')
