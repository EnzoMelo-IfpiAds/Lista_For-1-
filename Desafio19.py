# Leia N, calcule e escreva o valor de S. Questão 18
print("BEM-VINDO AO ENZOAPP")

print("=" * 35)
n = int(input("Coloque o N dos termos a ser calculado: "))
soma = 0
print("=" * 35)

for c in range(1, n + 1):
    S = 0
    if c % 2 == 0:
        S = - (n - c) / c 
    else:
        S = + c / (n - c)
    soma += S
    print("{:.2f}".format(soma))