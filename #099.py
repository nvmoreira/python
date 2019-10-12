"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

from time import sleep


def maior(* lista):
    print('-='*30)
    print('Analizando os valores passados...')
    if lista == ():
        print(f'Foram analizados 0 valores ao todo. \nO maior valor informado foi 0.')
    else:
        for i in lista:
            print(i, end=' ')
            sleep(.3)
        print(f'\nForam analisados {len(lista)} valores ao todo. \nO maior valor informado foi {max(lista)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()