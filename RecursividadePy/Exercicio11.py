def multiplicacao(n1, n2):
    if n2 == 0:
        return 0
    return n1 + multiplicacao(n1, n2 - 1)
