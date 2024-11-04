def numeros_pares_decrescentes(n):
    if n < 0:
        return
    if n % 2 == 0:
        print(n)
    numeros_pares_decrescentes(n - 1)
