def fatorial_duplo(n):
    if n == 1 or n == 0:
        return 1
    return n * fatorial_duplo(n - 2)
