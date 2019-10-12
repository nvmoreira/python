# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

x = float(input('Digite o valor do ângulo: '))

seno = math.sin(math.radians(x))
cosseno = math.cos(math.radians(x))
tangente = math.tan(math.radians(x))

print('Dado o ângulo {}, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}.'.format(x, seno, cosseno, tangente))