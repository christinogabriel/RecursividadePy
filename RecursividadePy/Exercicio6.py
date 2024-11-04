def potencia(k, n):
    if n == 0:
        return 1
    return k * potencia(k, n - 1)

k = int(input("Digite o valor de k: "))
n = int(input("Digite o valor de n: "))
resultado = potencia(k, n)
print(f"{k}^{n} = {resultado}")
