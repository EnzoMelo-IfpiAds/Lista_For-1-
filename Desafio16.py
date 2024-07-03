# Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci (0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.
print("BEM-VINDO AO ENZOAPP")

print("=" * 20)
n = int(input("Quantos números da sequência de fibonacci você quer calcular? "))
print("=" * 20)


for c in range(2, n + 1):
    if c >= 3:
        formula = (c - 1) + (c - 2)
        print(formula)
    else: 
        print('''1
1
2''')