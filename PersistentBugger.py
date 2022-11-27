def persistence(n):
    simple_list = []
    number_of_repetitions = 0
    while len(str(n)) >= 2:
        for i in range(len(str(n))):
            simple_list.append(int(str(n)[i]))
        n = eval(str(simple_list)[1:-1].replace(',', '*'))
        simple_list.clear()
        number_of_repetitions += 1
    return number_of_repetitions
