"""Faça un programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o menor e o maior
valor digitado e as suas respectivas posições na lista."""

numeros = []
for i in range(5):
    valor = int(input(f'Digite um número para a posição {i}: '))
    numeros.append(valor)
print(f'O maior número da lista é {max(numeros)} e está na posição ', end='')
for c, i in enumerate(numeros):
    if i == max(numeros):
        print(c, end=' ')
print(f'\nO menor número é {min(numeros)} e está na posição ', end='')
for c, i in enumerate(numeros):
    if i == min(numeros):
        print(c, end=' ')
