# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

x = int(input('Digite um número inteiro: '))

primo = 0
for i in range(1, x + 1):
    if x % i == 0:
        primo += 1
if primo == 2:
    print('O número {} é primo.'.format(x))
else:
    print('O número {} não é primo.'.format(x))