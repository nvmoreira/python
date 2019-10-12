"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

print('~'*15, 'CALCULADORA DE PREÇOS', '~'*15)
total = 0
caro = 0
menor = 0
barato = ''

while True:
    nome = input('Produto: ').upper().strip()
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        caro += 1
    if menor == 0:
        menor = preco
        barato = nome
    elif 0 < menor and menor > preco:
        menor = preco
        barato = nome
    cont = input('Deseja continuar [S/N]? ').upper().strip()
    if cont not in 'SN':
        cont = input('Opção inválida. Deseja continuar?')
    elif cont == 'N':
        print('--'*20)
        print(f'O total gasto foi R${total}.')
        print(f'O produto mais barato é o {barato} e custou R${menor}.')
        print(f'Temos {caro} produtos que custaram mais do que R$1000,00.')
        break
