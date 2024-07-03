# Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação,
# nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o
# numero de identificação e o peso do boi mais magro e do boi mais gordo.
print("BEM-VINDO AO ENZOAPP")

print("=" * 20)
n_fichas = int(input("Quantas fichas você quer ler? "))
mais_magro = 1000
mais_gordo = 0
numero_magro = 0
numero_gordo = 0
print("=" * 20)

for c in range(1, n_fichas + 1):
    numero = int(input("Qual o número de identificação desse boi? "))
    nome = str(input("Qual o nome de identificação desse boi? "))
    peso = float(input("Qual o peso(kg) desse boi? "))
    
    if peso < mais_magro:
        numero_magro = numero 
        mais_magro = peso
    if peso > mais_gordo:
        numero_gordo = numero
        mais_gordo = peso

print("O boi mais magro pesa {} e seu número de identificação é {}".format(mais_magro, numero_magro))
print("O boi mais gordo pesa {} e seu número de identificação é {}".format(mais_gordo, numero_gordo))
