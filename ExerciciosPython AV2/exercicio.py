#Questão 1

def calcule_area(baseMaior, baseMenor, altura):
    a = (baseMaior+baseMenor)*altura/2
    print(f'A área do trapézio é de {a}')


print('Área do Trapézio')
print('-'*20)
B = int(input('Digite o valor da Base Maior: '))
b = int(input('Digite o valor da Base Menor: '))
A = int(input('Digite o valor da Altura: '))
calcule_area(B,b,A)

#Questão 2

def soma_imposto(taxa_imposto,custo):
    precoProduto = custo*(taxa_imposto/100)+custo
    print(f'O valor do produto é R$ {precoProduto}')


print('Soma Imposto')
print('-'*20)
taxa = float(input('Digite o valor da taxa de imposto (%): '))
custo = float(input('Digite o valor de custo do produto: '))
soma_imposto(taxa,custo)

#Questão 3

def conversao(taxa_imposto,custo):
    
    print(f'O valor do produto é R$ {precoProduto}')


def saida(taxa_imposto,custo):
    
    print(f'O valor do produto é R$ {precoProduto}')