def inverter_numero(n):
    if n == 0:
        return 0
    else:
        return int(str(n % 10) + str(inverter_numero(n // 10)))
