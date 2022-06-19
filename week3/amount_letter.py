# First task
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0

for item in items:
    if 'w' in item:
        acc_num += 1
print(acc_num)

# Second task
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

list_sentence = sentence.split()
num_a_or_e = 0

for elem in list_sentence:
    if "a" in elem or "e" in elem:
        num_a_or_e += 1
print(num_a_or_e)

# Third task
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

num_vowels = 0

for i in s:
    if i in vowels:
        num_vowels += 1
print(num_vowels)


