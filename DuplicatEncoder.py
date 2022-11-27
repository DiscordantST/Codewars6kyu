def duplicate_encode(word):
    simple_list = []
    simple_list_reform = []
    for symbol in word:
        simple_list.append(symbol.lower())
    for i in range(len(simple_list)):
        if simple_list.count(simple_list[i].lower()) > 1:
            simple_list_reform.append(simple_list[i].lower().replace(simple_list[i].lower(), ")"))
        if simple_list.count(simple_list[i].lower()) == 1:
            simple_list_reform.append(simple_list[i].lower().replace(simple_list[i].lower(), "("))
    return "".join(simple_list_reform)

# another answer
#
# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])