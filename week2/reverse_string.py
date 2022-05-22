# Считать строку, вывести ее в обратном направлении АБВ - ВБА.

s = input('Input any string: ')

for i in range(len(s)-1, 0-1, -1):
    print(s[i], end='')

print()
print(s[::-1])
