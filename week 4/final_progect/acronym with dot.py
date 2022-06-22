stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

acro = ""
acronym = []

sent = sent.split()

for elem in sent:
    if elem in stopwords:
        acronym = []
    else:
        acro += elem[0:2]
        if elem != sent[-1]:
            acro += '. '
acro = acro.upper()
print(acro)