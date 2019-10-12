"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

x = int(input('Escreva o primeiro número inteiro: '))
y = int(input('Escreva o segundo número inteiro: '))

if x > y:
    print('O primeiro valor é maior.')
elif y > x:
    print("O segundo valor é maior.")
else:
    print('Não exste valor maior, os dois são iguais.')