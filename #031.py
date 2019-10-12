"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

km = float(input('Qual é a distância que você deseja percorrer? '))

if km <= 200:
    passagem = km * 0.5
    print('A passagem custa R${:.2f}.'.format(passagem))
else:
    passagem = km * 0.45
    print('A passagem custa R${:.2f}'.format(passagem))
