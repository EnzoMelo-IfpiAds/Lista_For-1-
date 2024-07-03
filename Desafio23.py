# Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de
# horas trabalhadas e o seu número de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
# 40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.
# Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N
# funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário líquido do funcionário.
print("BEM-VINDO AO ENZOAPP")

print("=" * 20)
n = int(input("Quantos funcionários entrarão no programa? "))
print("=" * 20)

for funcionario in range(1, n + 1):
    codigo = int(input("Qual o código desse funcionário? "))
    horas_trabalhadas = int(input("Número de horas trabalhadas dele: "))
    dependentes = int(input("Número de dependentes desse funcionário: "))

    hora = 12 * horas_trabalhadas
    dependente_pago = 40 * dependentes
    salario = hora + dependente_pago
    inss = salario * 0.085
    ir = salario * 0.05
    salario_liquido = salario - inss - ir

    print("Esse funcionário gasta {:.2f} R$ com INSS e {:.2f} R$ com IR.".format(inss, ir))
    print("Seu salário líquido é de {:.2f} R$".format(salario_liquido))
    print("-" * 20)