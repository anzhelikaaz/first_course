from datetime import datetime

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

t0 = datetime.now()
for _ in range(100000):
    for ch in s[:len(s) // 2]:
        print(ch, end='')
print(datetime.now() - t0)
# 00:01.920824

# t0 = datetime.now()
# for _ in range(100000):
#     for i in range(len(s) // 2):
#         print(s[i], end='')
# print(datetime.now() - t0)
# 0:00:02.074452

# t0 = datetime.now()
# for _ in range(100000):
#     print(s[len(s) // 2:])
# print(datetime.now() - t0)
# 0:00:01.125987

# t0 = datetime.now()
# for _ in range(100000):
#     print(first_part(s))
# print(datetime.now() - t0)
# # 0:00:01.873350
