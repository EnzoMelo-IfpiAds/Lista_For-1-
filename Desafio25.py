# Em uma eleição presidencial existem 3 (três) candidatos. Os votos são informados através de códigos.
# Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
# · 1, 2, 3 = voto para os respectivos candidatos;
# · 9 = voto nulo;
# · 0 = voto em branco;
# Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva:
# a) total de votos para cada candidato;
# b) total de votos nulos;
# c) total de votos em branco;
# d) quem venceu a eleição.
print("BEM-VINDO AO ENZOAPP")

print("=" * 20)
eleitores = int(input("Quantos eleitores vão votar? "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
nulo = 0
branco = 0
print("-=" * 20)
print(''' Lembre-se que:
. Candidato 1 é o número 1
. Candidato 2 é o número 2
. Candidato 3 é o número 3
. Voto NULO é o número 9
. voto EM BRANCO é o número 0
= BOA SORTE!!''')
print("-=" * 20)
print("=" * 20)

for c in range(1, eleitores + 1):
    voto = int(input("Insira o número do voto: "))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 9:
        nulo += 1
    elif voto == 0:
        branco += 1
    else:
        print("Voto inválido.")

print('''   TOTAL DE VOTOS  
=========================
Candidato 1: {} Voto(s).
Candidato 2: {} Voto(s).
Candidato 3: {} Voto(s).
Votos NULOS: {} Voto(s).
Votos BRANCOS: {} Voto(s).
========================='''.format(candidato1,candidato2,candidato3,nulo,branco))

if candidato1 > candidato2 and candidato1 > candidato3:
    print("O vencedor foi o CANDIDATO 1!")
elif candidato2 > candidato1 and candidato2 > candidato3:
    print("O vencedor foi o CANDIDATO 2!")
elif candidato3 > candidato1 and candidato3 > candidato2:
    print("O vencedor foi o CANDIDATO 3!")
else:
    print("NÃO HOUVE VENCEDOR, HAVERÁ NOVA ELEIÇÃO.")