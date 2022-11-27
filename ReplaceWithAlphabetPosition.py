def alphabet_position(text):
    simple_dict = dict(zip('abcdefghijklmnopqrstuvwxyz', range(1, 27)))
    c = []
    text1 = text.lower()
    for i in range(len(text1)):
        c.append(simple_dict.get(text1[i]))
    return " ".join(map(str, [c for c in c if c != None]))

