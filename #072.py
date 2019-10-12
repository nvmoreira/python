"""Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

while True:
    contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    numero = int(input('Digite um número de 0 a 20: '))
    print(f'Você digitou o número {contagem[numero]}.')
    if numero > 20:
        print('Opção inválida.')
    cont = input('Deseja digitar outro número [S/N]? ').strip().upper()
    if cont not in 'SN':
        print('Opção inválida.')
    elif cont == 'N':
        print('Até a próxima!')
        break
