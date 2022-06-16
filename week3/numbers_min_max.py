# Напишите программу, которая получает на вход три целых числа,
# по одному числу в строке, и выводит на консоль в три строки
# сначала максимальное, потом минимальное,
# после чего - оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a == b == c:
    maxi, mini, medi = a, c, b

if a >= b > c:
    maxi, mini, medi = a, c, b

elif a >= c >= b:
    maxi, mini, medi = a, b, c

elif b > a > c:
    maxi, mini, medi = b, c, a

elif b >= c >= a:
    maxi, mini, medi = b, a, c

elif c > a > b:
    maxi, mini, medi = c, b, a

elif c > b >= a:
    maxi, mini, medi = c, a, b

print(maxi, mini, medi, sep='\n')