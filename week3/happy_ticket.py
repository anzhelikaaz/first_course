'''
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
На вход программе подаётся строка из шести цифр.
Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

'''

num_ticket = input('Введите номер билета: ')

l_ticket = len(num_ticket)

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


