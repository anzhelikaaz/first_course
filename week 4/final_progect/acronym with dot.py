stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

acro = ""

sent = sent.split()

for elem in sent:
    if elem not in stopwords:
        acro += elem[0:2]
        if elem != sent[-1]:
            acro += '. '
acro = acro.upper()
print(acro)