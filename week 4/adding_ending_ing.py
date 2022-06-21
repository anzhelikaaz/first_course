#  Adding of ending 'ing' to words in the list with accumulator pattern, loop.
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
ending = 'ing'

for verb in verbs:
    verb += ending
    ing.append(verb)
print(ing)

#  Adding of ending 'ed' to words in the list with append, loop.
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
ending = 'ed'

for elem in wrds:
    past_wrds.append(elem + ending)
print(past_wrds)
