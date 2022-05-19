from scipy.spatial import distance


num_elements = int(input('Number of elements in the lists: '))
a = []
b = []

for i in range(num_elements):
    x = float(input('Input elements of the first list: '))
    y = float(input('Input elements of the second list: '))
    a.append(x)
    b.append(y)
print(a, b)

print('Equal lengths of vectors: ', len(a) == len(b))

scalar_product = 0
norm_a = 0
norm_b = 0

for i in range(len(a)):
    scalar_product = scalar_product + a[i] * b[i]
    norm_a = norm_a + a[i] ** 2
    norm_b = norm_b + b[i] ** 2

norm_a = norm_a ** 0.5
norm_b = norm_b ** 0.5

result = scalar_product / (norm_a * norm_b)
print(1 - result)

right_dist_cosine = distance.cosine(a, b)
print(round(right_dist_cosine, 3) == round(1 - result, 3))
