"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo*-1} em {passo*-1}')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
    if fim < inicio and passo > 0:
        passo *= -1
    contagem = inicio
    while True:
        print(contagem, end=' ')
        contagem += passo
        sleep(.5)
        if inicio > fim > contagem or inicio < fim < contagem:
            break
    print('FIM!')
    sleep(.5)
    print('-='*40)


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
