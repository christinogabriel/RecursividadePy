def numeros_crescentes(n):
    if n < 0:
        return
    numeros_crescentes(n - 1)
    print(n)
