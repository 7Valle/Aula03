compra = float(input('\nInforme o valor da compra: '))

if compra > 250:
    desconto = compra * 0.16
    print(f'\nO total da compra é R$ {compra - desconto}!')
else:
    print(f'\nO total da compra é R$ {compra}.') 