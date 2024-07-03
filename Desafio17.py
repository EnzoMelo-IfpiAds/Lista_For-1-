# Leia N, calcule e escreva o valor de S. Questão 17
print("BEM-VINDO AO ENZOAPP")

print("=" * 30)
n = int(input("Coloque o limite, ou seja, N termos: "))
soma = 0
print("=" * 30)

"Cálculo das frações 1/S"
for c in range(1, n):
    S = 1/c
    soma += S
    print("{:.2f}".format(soma))