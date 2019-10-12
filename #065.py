"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores."""

cont = 'S'
i = 0
soma = 0
media = 0
maior = 0
menor = 0

while cont != 'N':
    x = int(input('Digite um número inteiro: '))
    i += 1
    soma += x
    media = soma / i
    if maior < x:
        maior = x
    if menor == 0 or menor > x:
        menor = x
    cont = input('Você deseja digitar outro número [S/N]? ').strip().upper()
    if cont not in 'SN':
        print('Comando inválido.')
        cont = input('Você deseja digitar outro número [S/N]? ').strip().upper()
    elif cont == 'N':
        print('A média dos valores lidos foi {:.2f}, sendo o menor valor {} e o maior {}.'.format(media, menor, maior))
