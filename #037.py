"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

x = int(input('Escreva um número inteiro: '))
y = int(input("""As base de conversão são:
1 - binário
2 - octal
3 = hexadecimal
Escolha sua opção: """))

if y == 1:
    print('O número {} corresponde a {} em binário.'.format(x, bin(x)[2:]))
elif y == 2:
    print('O número {} corresponde a {} em octal.'.format(x, oct(x)[2:]))
else:
    print('O número {} corresponde à {} em hexadecimal.'.format(x, hex(x)[2:]))