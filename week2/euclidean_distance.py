a = [4, 5, 6, 7, 8, 2, 1, 3, 25, 35]
b = [77, 23, 43, 56, 63, 9, 32, 5, 21, 34]
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arr_sum = 0

print('Equal lengths of vectors: ', len(a) == len(b))

for i in range(len(a)):
    c[i] = (b[i] - a[i]) ** 2
    arr_sum = arr_sum + c[i]

distance = arr_sum ** 0.5
print('Euclidean distance between vectors:', round(distance, 3))
