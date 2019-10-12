# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
# calcule e mostre o comprimento da hipotenusa.

import math
x = float(input('Digite o valor do cateto oposto: '))
y = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.hypot(x, y)

print('O valor da hipotenusa é {}.'.format(hipotenusa))
