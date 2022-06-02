# one for loop to print out each character of the string my_str
my_str = "MICHIGAN"
for char in my_str:
    print(char)

# two for loop to print out each character of the string and type
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
for char in several_things:
    print(char)

for type_char in several_things:
    print(type(type_char))

# code that uses iteration to print out the length of each element of the list stored in str_list.
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

for w in str_list:
    num = len(w)
    print(num)

# count the number of characters in original_str using the accumulation pattern
original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0

for elem in original_str:
    num_chars += 1
print(num_chars)

# the accumulation pattern to take the sum of all of the numbers
addition_str = "2+5+10+20"
x = addition_str.split("+")
n = len(x)
sum_val = 0

for i in range(n):
    x[i] = int(x[i])
    sum_val += x[i]
print(sum_val)

