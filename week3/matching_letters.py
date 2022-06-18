# Необходимо проверить, сколько слов в строке имеют одинаковыми первые и последние буквы.
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

list_sentence = sentence.split()

same_letter_count = 0

for elem in list_sentence:
    if elem[0] == elem[-1]:
        same_letter_count += 1
print(same_letter_count)
