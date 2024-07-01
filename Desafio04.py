# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Geométrica que tem por valor inicial A0 e razão R.
print("BEM-VINDO AO ENZOAPP")

print("=" * 35)
a0 = int(input("Por favor, coloque o valor de A0: "))
limite = int(input("Agora, coloque o limite da PG: "))
razao = int(input("Por último, coloque a razão da PG: "))
print("=" * 35)

for c in range(a0, limite):
    pg = a0 * razao**(c - 1)
    print(pg)