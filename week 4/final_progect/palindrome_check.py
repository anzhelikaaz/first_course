# A palindrome is a phrase that, if reversed, would read the exact same.
# Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original.
# Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.

p_phrase = "was it a car or a cat I saw"
r_phrase = ''

p_phrase_new = p_phrase.replace(' ', '')
p_phrase_new = p_phrase_new.lower()

# Solving with loop
# for i in range(len(p_phrase_new) - 1, -1, -1):
#     r_phrase += p_phrase_new[i]

# Solving with slice
r_phrase = p_phrase_new[::-1]
print(r_phrase)

if p_phrase_new == r_phrase:
    print(True)

