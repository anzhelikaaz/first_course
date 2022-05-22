def first_part(x):
    return x[:len(x) // 2]


s = '123456789'

#displaying a half of the list
print(s[:len(s) // 2], first_part(s))
print(s[len(s) // 2:], first_part(s[::-1])[::-1])

#displaying a quarter of the list
print(type(first_part(s[::-1])))
print(s[:len(s) // 4], first_part(s[:len(s) // 2]),
      first_part(first_part(s)))

#displaying a half of the list by loops
for i in range(len(s) // 2):
    print(s[i], end='')

print()

for ch in s[:len(s) // 2]:
    print(ch, end='')
