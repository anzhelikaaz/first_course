#Напишите программу, которая по данному числу N от 1 до 9 выводит на экран N пингвинов.
# Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами также имеется пустой (из пробелов) столбец.
# Разрешается вывести пустой столбец после последнего пингвина.
# Для упрощения рисования скопируйте пингвина из примера в среду разработки.

n = int(input('Number of the penguins from 1 to 9: ', ))

# making a penguin by loop and tuple
elements_p = ('     _~_     ',
              '    (o o)    ',
              '   /  V  \   ',
              '  /(  _  )\  ',
              '    ^^ ^^    ')

for i in range(len(elements_p)):
    print(elements_p[i] * n)

# other way of loop without using index
for elem_p in elements_p:
    print(elem_p * n)

# making a penguin by print
print(
'     _~_     ' * n,
'    (o o)    ' * n,
'   /  V  \   ' * n,
'  /(  _  )\  ' * n,
'    ^^ ^^    ' * n, sep='\n' )



