# Leia N, calcule e escreva o valor de S. Questão 18
print("BEM-VINDO AO ENZOAPP")

print("=" * 35)
n = int(input("Coloque o N dos termos a ser calculado: "))
numerador = 0
soma = 0
print("=" * 35)

for c in range(1, n + 1):
    if c % 2 == 1:
        numerador += c
    S = numerador / c
    soma += S
    print("{:.2f}".format(soma))