def find_outlier(integers):
    odd = []
    even = []
    for i in integers:
        if i % 2 == 0:
            odd.append(i)
        if i % 2 != 0:
            even.append(i)
    return odd[0] if len(odd) == 1 else even[0]
