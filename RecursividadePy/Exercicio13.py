def numeros_decrescentes(n):
    if n < 0:
        return
    print(n)
    numeros_decrescentes(n - 1)
