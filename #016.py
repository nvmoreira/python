# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
x = float(input('Digite um número Real: '))

inteiro = math.trunc(x)

print('A parte inteira de {} é {}.'.format(x, inteiro))