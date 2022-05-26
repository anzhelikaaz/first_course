# input = 9 5 6
# input = 1 0 0
# out = 1056

first_string = input('Input digits in the list: ')
second_string = input('Input digits in the other list: ')
array1 = first_string.split()
array2 = second_string.split()

first_string = ''.join(array1)
second_string = ''.join(array2)

x1 = int(first_string)
x2 = int(second_string)

print(x1 + x2)

