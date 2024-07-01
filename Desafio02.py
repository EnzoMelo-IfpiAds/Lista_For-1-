# Leia N e escreva todos os números inteiros pares de 1 a N.
print("BEM-VINDO AO ENZOAPP")

print("=" * 20)
n = int(input("Coloque o valor de N: "))
print("=" * 20)

print("Números pares de 1 até {}".format(n))
for c in range(1, n + 1):
    if c % 2 == 0:
        print(c)