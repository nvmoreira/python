""" Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores."""

from datetime import date

maior = 0
menor = 0
for i in range(1, 8):
    x = int(input('Digite o {}º ano: '.format(i)))
    if date.today().year - x >= 18:
        maior += 1
    else:
        menor += 1
if maior == 0:
    print('Nenhuma pessoa atingiu a maioridade.')
elif menor == 0:
    print('Todas as pessoas já atingiram a maioridade.')
else:
    print('Das 7 pessoas, {} já atingiram a maioridade e {} ainda são menores.'.format(maior, menor))