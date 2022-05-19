num_elements = int(input('Number of elements in the lists: '))
a = []
b = []

for i in range(num_elements):
    x = float(input('Input elements of the first list: '))
    y = float(input('Input elements of the second list: '))
    a.append(x)
    b.append(y)
print(a, b)

c = list(range(num_elements))
arr_sum = 0

print('Equal lengths of vectors: ', len(a) == len(b))

for i in range(len(a)):
    c[i] = (b[i] - a[i]) ** 2
    arr_sum = arr_sum + c[i]

distance = arr_sum ** 0.5
print('Euclidean distance between vectors:', round(distance, 3))
