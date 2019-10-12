"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while."""

x = int(input('Digite o primeiro termo da PA: '))
y = int(input('Digite a razão da PA: '))

i = 0

print('Os dez primeiros termos da PA são: ', end='')

while i < 9:
    print(x, ', ', end='')
    x += y
    i += 1
print('{}.'.format(x))
