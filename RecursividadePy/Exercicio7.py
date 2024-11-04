def inverter_vetor(vetor):
    if len(vetor) == 0:
        return []
    return [vetor[-1]] + inverter_vetor(vetor[:-1])

vetor = [i for i in range(100)]
vetor_invertido = inverter_vetor(vetor)
print(vetor_invertido)
