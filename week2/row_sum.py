# Считываем число с клавиатуры, выводим арифметическую запись, например, при 5 - (1+2+3+4+5).

c = int(input('Input random number: '))
arr_sum = 0

for i in range(1, c+1):
    arr_sum += i
    print('+', i, end=' ')

print('=', arr_sum)