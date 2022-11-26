def spin_words(sentence):
    d = []
    for i in range(int(len(sentence.split()))):
        if len(sentence.split()[i]) < 5:
            d.append(sentence.split()[i])
        if len(sentence.split()[i]) >= 5:
            d.append(sentence.split()[i][::-1])
    return " ".join(d)

