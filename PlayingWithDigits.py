def dig_pow(n, p):
    simple_string_for_exp = ""  # add digit from n ** p + n ** p + 1 (string)
    exp = 0  # add digit from n ** p + n ** p + 1 (int)
    simple_digit = 0  # add exp + exp
    for i in range(0 , len(str(n))):
        exp = int(str(n)[i]) ** (p + i)
        simple_digit += exp
    simple_string_for_exp += str(int(simple_digit))
    if int(simple_string_for_exp) % n == 0:
        return int(int(simple_string_for_exp) / n)
    else:
        return -1
