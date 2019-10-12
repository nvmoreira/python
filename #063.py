"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
Sequência de Fibonacci. (0 - 1 - 1 - 2 - 3 - 5 - 8)"""

x = int(input('Quantos números da Sequência de Fibonacci você deseja ver? '))

i = 1
pen = 0
ult = 1
sequencia = 0
print(pen, '→ ', end=' ')

while i < x:
    print(ult, '→ ', end=' ')
    sequencia = pen + ult
    pen = ult
    ult = sequencia
    i += 1
print('FIM')
