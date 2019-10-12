"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
triângulo.
Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos
outros dois e maior que o valor absoluto da diferença entre essas medidas
"""

x = float(input('Digite o tamanho da primeira reta: '))
y = float(input('Digite o tamanho da segunda reta: '))
z = float(input('Diigite o tamanho da terceira reta: '))

if y + z > x > int(y - z) and x > int(z - y) or x + z > y > int(x - z) and y > int(z - x) or x + y > z > int(y - x) \
        and z > int(x - y):
    print('As retas podem formar um triângulo.')
else:
    print('As retas NÃO podem formar um triângulo.')