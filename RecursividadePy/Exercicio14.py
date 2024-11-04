def numeros_pares_crescentes(n):
    if n < 0:
        return
    if n % 2 == 0:
        numeros_pares_crescentes(n - 2)
        print(n)
    else:
        numeros_pares_crescentes(n - 1)
