"""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print('-'*20)
print('{:^20}'.format('BANCO NATYZINHA'))
print('-'*20)
cinq = vinte = dez = um = 0

while True:
    saque = int(input('Quanto quer sacar? R$ '))
    cinq = saque // 50
    vinte = saque % 50 // 20
    dez = saque % 50 % 20 // 10
    um = saque % 10
    print(f'Cédulas de R$50: {cinq} \nCédulas de R$20: {vinte} \nCédulas de R$10: {dez} \nCédulas: de R$1: {um}')
    print('~'*20)
    cont = input('Deseja realiza outro saque [S/N]? ').upper().strip()
    if cont not in 'SN':
        cont = input('Opção inválida. \nDeseja realizar outro saque [S/N]? ')
    elif cont == 'N':
        break
