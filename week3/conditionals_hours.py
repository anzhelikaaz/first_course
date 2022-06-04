A = int(input('Минимальное количество часов сна: '))
B = int(input("Избыток часов сна: "))
H = int(input("Сколько вы спите? "))

if H >= A and H <= B:
    print('Это нормально')
elif H < A:
    print('Недосып')
elif H > B:
    print('Пересып')
