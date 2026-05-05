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