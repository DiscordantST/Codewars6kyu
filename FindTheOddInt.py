def find_it(seq):
    a = (set([x for x in seq if seq.count(x) % 2 != 0]))
    return list(a)[0]


#  another answer
#  return [x for x in seq if seq.count(x) % 2][0]
