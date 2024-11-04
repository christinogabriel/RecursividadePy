def contar_digitos(n, k):
    if n == 0:
        return 1 if k == 0 else 0
    return (1 if n % 10 == k else 0) + contar_digitos(n // 10, k)
