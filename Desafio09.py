# Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.
print("BEM-VINDO AO ENZOAPP")

print("=" * 18)
limiteSuperior = int(input("Coloque o valor do limite superior: "))
limiteInferior = int(input("Coloque o valor do limite inferior: "))
print("=" * 18)

for c in range(limiteInferior, limiteSuperior):
    if c % 2 == 0:
        print(c)