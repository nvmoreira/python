"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

dados = []
pessoas = []
maior = 0
menor = 0

while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    cont = input('Deseja continuar [S/N]? ').upper().strip()
    if cont == 'N':
        print(f'Foram cadastradas {len(pessoas)} pessoas.')
        print(f'O maior peso foi {maior}kg de ', end='')
        for i in pessoas:
            if i[1] == maior:
                print(f'{i[0]}', end=' ')
        print(f'\nO menor peso foi {menor}kg de ', end='')
        for i in pessoas:
            if i[1] == menor:
                print(i[0], end=' ')
        break
    for i in pessoas:
        if i[1] >= maior:
            maior = i[1]
        if menor == 0:
            menor = i[1]
        elif 0 < menor and i[1] <= menor:
            menor = i[1]
