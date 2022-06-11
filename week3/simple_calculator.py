a = float(input("Введите любое целое число: "))
b = float(input("Введите любое целое число: "))
c = (input("Введите операцию(возможные: +, -, /, *, mod, pow, div):  "))

if b == 0 and (c == "div" or c == "mod" or c == "/"):
    print('Деление на 0!')
if c == "+":
    print(a + b)
if c == "-":
    print(a - b)
if c == "/" and b != 0:
    print(a / b)
if c == "*":
    print(a * b)
if c == "pow":
    print(a ** b)
if c == "div" and b != 0:
    print(a // b)
if c == "mod" and b != 0:
    print(a % b)