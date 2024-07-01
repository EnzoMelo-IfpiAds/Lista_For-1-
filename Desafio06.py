# Escreva a tabuada dos números de 1 a 10.
print("BEM-VINDO AO ENZOAPP")

print("-=" * 12)
n = int(input("Coloque um número: "))
print("-=" * 12)

print("Calculando tabuada de {}".format(n))
print("=" * 18)
for c in range(1,11):
    print("{} X {} = {}".format(n, c, n * c))
print("=" * 18)
