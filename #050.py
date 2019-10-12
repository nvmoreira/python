# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for i in range(1, 7):
    x = int(input('Digite o {}º valor inteiro: '.format(i)))
    if x % 2 == 0:
        soma = soma + x
        cont += 1
if soma != 0:
    print('A soma dos {} números pares digitados é {}.'.format(cont, soma))
else:
    print('Nenhum número par foi digitado.')
