#  Adding of ending 'ing' to words in the list with accumulator pattern, loop.
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
ending = 'ing'

for verb in verbs:
    verb += ending
    ing.append(verb)
print(ing)