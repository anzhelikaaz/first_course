count_progger = input('Сколько программистов в комнате? ')
sym_count = len(count_progger)

assert int(count_progger) >= 0, 'Ошибка! Введите неотрицательное число.'

last_one = count_progger[-1]

if sym_count >= 2 and count_progger[-2:] in ('11', '12', '13', '14'):
    end_word = 'ов'

elif last_one == '1':
    end_word = ''

elif last_one in ('2', '3', '4'):
    end_word = 'a'

elif last_one in ('5', '6', '7', '8', '9', '0'):
    end_word = 'ов'

print(count_progger, "программист" + end_word)
