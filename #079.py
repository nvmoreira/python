"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro ele não será adicionado. No final serão exibidos todos os valores únicos digitados em ordem
crescente"""

numeros = []
while True:
    cont = input('Deseja digitar um número? [S/N]').strip().upper()
    while cont not in 'SN':
        print('Opção inválida')
        cont = input('Deseja digitar um número? [S/N]').strip().upper()
    if cont == 'N':
        print(f'Os números digitados foram:  \n{numeros.sort()}')
        break
    x = int(input('Digite um número: '))
    if x not in numeros:
        numeros.append(x)
    else:
        print('Número duplicado!')
