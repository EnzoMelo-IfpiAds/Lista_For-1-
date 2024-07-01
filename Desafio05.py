#Leia um número, calcule e escreva seu fatorial.
print("BEM-VINDO AO ENZOAPP")

n = int(input("Coloque o número N: "))
count = n
f = 1

print('Calculando {}!'.format(n))
while count > 1:
    print("X {} =".format(count))
    f *= count
    count -= 1
    print("=" * 10)
    print('{}'.format(f))
    print("=" * 10)
