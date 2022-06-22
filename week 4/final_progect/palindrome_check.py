# A palindrome is a phrase that, if reversed, would read the exact same.
# Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original.
# Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.

p_phrase = "was it a car or a cat I saw"
r_phrase = ''

p_phrase_new = p_phrase.replace(' ', '')
p_phrase_new = p_phrase_new.lower()

for i in range(len(p_phrase) - 1, 0 - 1, -1):
    r_phrase += p_phrase[i]

r_phrase = r_phrase.replace(' ', '')
r_phrase = r_phrase.lower()
if p_phrase_new == r_phrase:
    print(True)