# Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.
print("BEM-VINDO AO ENZOAPP")

print("=" * 20)
limiteInferior = int(input("Coloque o valor do limite inferior: "))
limiteSuperior = int(input("Coloque o valor do limite superior: "))
print("=" * 20)

for c in range(limiteInferior, limiteSuperior):
    if c % c == 0:
        print(c)