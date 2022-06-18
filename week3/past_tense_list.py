words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_full = 'ed'
past_short = 'd'

past_tense = []

for word in words:
    if word[-1] == 'e':
        word += past_short
    else:
        word += past_full
    past_tense.append(word)
print(past_tense)
