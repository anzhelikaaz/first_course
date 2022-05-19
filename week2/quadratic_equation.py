a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = (b ** 2) - (4 * a * c)
print(d)

x1 = (-b + (d ** 0.5)) / 2 * a
print("The first unknown: ", x1)

x2 = (-b - (d ** 0.5)) / 2 * a
print("The second unknown: ", x2)

print(a, '* x^2 +', b, '* x +', c, '= 0')
