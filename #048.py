"""Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
intervalo de 1 até 500."""

contagem = 0
soma = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        contagem += 1
        soma = soma + i
print('A soma dos {} múltiplos ímpares de 3 entre 1 e 500 é {}.'.format(contagem, soma))