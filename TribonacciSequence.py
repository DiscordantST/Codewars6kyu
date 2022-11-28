def tribonacci(signature, n):
    signature_sum = []
    i = 0
    while len(signature_sum) < n:
        i = sum(signature[:])
        signature.append(i)
        signature_sum.append(signature.pop(0))
    return signature_sum






