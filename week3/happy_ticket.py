'''
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
На вход программе подаётся строка из шести цифр.
Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
'''

num_ticket = list(input('Введите номер билета: '))

# The first way of solving (simple)
first_num = num_ticket[0]
second_num = num_ticket[1]
third_num = num_ticket[2]
fourth_num = num_ticket[3]
fifth_num = num_ticket[4]
sixth_num = num_ticket[5]

first_num = int(first_num)
second_num = int(second_num)
third_num = int(third_num)
fourth_num = int(fourth_num)
fifth_num = int(fifth_num)
sixth_num = int(sixth_num)

if (first_num + second_num + third_num) == (fourth_num + fifth_num + sixth_num):
    print("Счастливый")

elif (first_num + second_num + third_num) != (fourth_num + fifth_num + sixth_num):
    print("Обычный")

# Second way of solving
sum_first_part = 0  # num_ticket[0:3]
sum_second_part = 0  # num_ticket[3:]

for i in range(3):
    sum_first_part += int(num_ticket[i])
    sum_second_part += int(num_ticket[3 + i])

if sum_first_part == sum_second_part:
    print('Счастливый')
else:
    print('Обычный')

# Third way of solving
l = list(map(int, list(input())))
if sum(l[:3]) == sum(l[3:]):
    print('Счастливый')
else:
    print('Обычный')
