# Leia N, calcule e escreva o valor de S. Questão 18
print("BEM-VINDO AO ENZOAPP")

print("=" * 35)
n = int(input("Coloque o N dos termos a ser calculado: "))
soma = 0
print("=" * 35)

"Cálculo das frações 1/S"
for c in range(1, n):
    S = c / ( n - c)
    soma += S 
    print("{:.2f}".format(soma))