words = ["water", "chair", "pen", "basket", "hi", "car"]

num_words = 0
for elem in words:
    if len(elem) > 3:
        num_words += 1

print(num_words)
