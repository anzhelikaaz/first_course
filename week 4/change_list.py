#  Change list without append method.
numbs = [5, 10, 15, 20, 25]
index = 0

for num in numbs:
    num += 5
    numbs[index] = num
    index += 1
print(numbs)