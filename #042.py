"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""

x = float(input('Digite o tamanho da primeira reta: '))
y = float(input('Digite o tamanho da segunda reta: '))
z = float(input('Diigite o tamanho da terceira reta: '))

if y+z > x > int(y-z) and x > int(z-y) or x+z > y > int(x-z) and y > int(z-x) or x + y > z > int(y-x) and z > int(x-y):
    print('As retas podem formar um triângulo ', end='')
    if x == y == z:
        print('EQUILÁTERO')
    elif x == y or x == z or y == z:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('As retas NÃO podem formar um triângulo.')
