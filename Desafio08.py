# Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.
print("BEM-VINDO AO ENZOAPP")

print("=" * 18)
n = int(input("Coloque o valor de N: "))
limiteSuperior = int(input("Coloque o valor do limite superior: "))
limiteInferior = int(input("Coloque o valor do limite inferior: "))
print("=" * 18)

print("Calculando os múltiplos de {} dentro dos limites".format(n))
print("=" * 18)
for c in range(limiteInferior, limiteSuperior):
    if c % n == 0:
        print(c)
print("=" * 18)
