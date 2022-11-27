def duplicate_count(text):
    simple_list = []
    simple_set = set()
    for symbol in text:
        simple_list.append(symbol.lower())
    for i in range(len(simple_list)):
        if simple_list.count(simple_list[i]) > 1:
            simple_set.add(simple_list[i])
    return len(simple_set)
