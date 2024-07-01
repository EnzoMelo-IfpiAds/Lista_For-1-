# Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.
print("BEM-VINDO AO ENZOAPP")

print("=" * 20)
limiteSuperior = int(input("Coloque o valor do limite superior: "))
limiteInferior = int(input("Coloque o valor do limite inferior: "))
print("=" * 20)

print("Definindo números ímpares entre {} e {} :".format(limiteInferior, limiteSuperior))
for c in range(limiteInferior, limiteSuperior):
    if c % 2 == 1:
        print(c)