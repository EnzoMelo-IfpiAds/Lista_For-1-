# Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.
print("BEM-VINDO AO ENZOAPP")

print("=" * 25)
n = int(input("Coloque o valor de N: "))
limite = int(input("Coloque um limite de número superior para a lista(o programa encerrará quando chegar nesse limite da lista): "))
soma = n
media = 0
print("=" * 25)

for c in range(n, limite):
    n2 = int(input("Colocar o valor do próximo número da lista: "))
    if c != 0:
        soma += n2
        media = soma / limite
        print("A soma dos termos é {}".format(soma))
        print("A média dos termos é {:.2f}".format(media))
    else:
        print("Você finalizou o programa,volte sempre!!")