#Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Aritmética que tem por valor inicial A0 e razão R.
print("BEM-VINDO AO ENZOAPP")

print("=" * 20)
a0 = int(input("Por favor, coloque o A0 da P.A: "))
limite = int(input("Agora,coloque o limite da P.A: "))
razao = int(input("Por último,coloque a razão da P.A: "))
print("=" * 20)

for c in range (a0, limite, razao):
    print(c)