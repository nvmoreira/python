# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    elif menor == 0:
        menor = peso
    elif menor > peso:
        menor = peso

print('O maior peso é {}kg e o menor é {}kg.'.format(maior, menor))