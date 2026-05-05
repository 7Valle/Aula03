idade = int(input('\nDigita a idade: '))

#Sinais de comparação: >, <, <=, >=, ==, !=
if idade >= 18:
    print('Você é maior!')
else:
    print('Você é menor de idade!')
#---------------------------------------

#Classificação por pontos:
    # Se pontos >=100, ganha mais 10 pontos
    # >=50 = 5
    # <50 = 0

pontos = int(input('\nInforme os pontos: '))
if pontos >= 100:
    total = pontos + 10
    print(f'\nExcelente! Agora você têm {total} pontos!')
elif pontos >= 50:
    total = pontos + 5
    print(f'\nBom desempenho. Você têm {total} pontos.')
else:
    print(f'\nContinue treinando. Sua pontuação atual é {pontos}.')

print('\nFim!')
