# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
# número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e escreva:
# a) média de salário da população;
# b) média de número de filhos;
# c) percentual de pessoas com salário de até R$ 1.000,00.
print('BEM-VINDO AO ENZOAPPP')

print("=" * 20)
habitantes = int(input("Escreva o número de habitantes na pesquisa: "))
salario_populacao = 0
totais_filhos = 0
salario_ate_1000 = 0
print("=" * 20)

for c in range(1, habitantes + 1):
    salario = float(input("Qual o salário desse habitante? "))
    filhos = int(input("Número de filhos dele: "))
    
    salario_populacao += salario
    totais_filhos += filhos

    if salario <= 1000:
        salario_ate_1000 += 1
    
    media_salarial = salario_populacao / habitantes
    media_filhos = totais_filhos / habitantes
    percentual_salario_ate_1000 = (salario_ate_1000 / habitantes) * 100

print("A média de salário da população é de {:.2f} R$".format(media_salarial))
print("A média do número de filhos na população é de {:.2f} por habitante".format(media_filhos))
print("A porcentagem de pessoas com salário de até 1000 R$ é {:.2f}".format(percentual_salario_ate_1000))