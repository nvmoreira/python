"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

data = int(input('Escreva seu ano de nascimento: '))

alistamento = int(date.today().year) - data

if alistamento < 18:
    tempo = 18 - alistamento
    print('Ainda não é hora de se alistar ao seviço militar. Faltam {} anos.'.format(tempo))
elif alistamento == 18:
    print('Está na hora de você se alistar ao serviço militar')
else:
    tempo = alistamento - 18
    print('Já passou da hora de você se alistar ao serviço militar. Você deveria ter se alistado há {} anos.'.format(tempo))