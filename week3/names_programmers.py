count_progger = input('Сколько программистов в комнате? ')
sym_count = len(count_progger)

assert int(count_progger) >= 0, 'Ошибка! Введите неотрицательное число.'

last_one = count_progger[-1]

if sym_count >= 2 and count_progger[-2:] in ('11', '12', '13', '14'):
    print(count_progger, "программистов")

elif last_one == '1':
    print(count_progger, "программист")

elif last_one in ('2', '3', '4'):
    print(count_progger, "программиста")

elif last_one in ('5', '6', '7', '8', '9', '0'):
    print(count_progger, "программистов")
