# Faça um programa que leia um número qualquer e mostre o seu fatorial.

x = int(input('Digite um número para calcular seu fatorial: '))

i = x
fatorial = 1
print('{}! = '.format(x), end='')

while i > 1:
    print(i, 'x ', end='')
    fatorial *= i
    i -= 1
print('1 = {}'.format(fatorial))
