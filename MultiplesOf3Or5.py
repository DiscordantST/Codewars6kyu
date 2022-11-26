def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum


# one line answer:
# return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

