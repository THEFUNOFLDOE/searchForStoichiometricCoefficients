def nsd(a, b):
    if a == 0 or b == 0:
        return 1

    while b:
        a, b = b, a % b
    return a


def nsk(a, b):
    return a * b // nsd(a, b)
