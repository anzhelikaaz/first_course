# 1 way
string = input('Input integer digits for array: ')
print(string, type(string))
array = string.split()
n = len(array)
summa = 0
for i in range(n):
    array[i] = int(array[i])
    summa += array[i]
print(array, summa)

# 2 way
print(
    sum(
        list(
            map(
                int,
                input('Input integer digits for array: ').split()
            )
        )
    )
)

# 3 way
print(
    sum(
        [int(x) for x in input('Input integer digits for array: ').split()]
    )
)
