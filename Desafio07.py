# Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.
print("BEM-VINDO AO ENZOAPP")

print("=" * 15)
n = int(input("Coloque o número N: "))
count = 0
print("=" * 15)

print("Somando números inteiros entre 1 e {}".format(n))
print("=" * 15)
for c in range(1, n):
    count += n
    print(count)
print("=" * 15)