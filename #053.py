# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print('{:=^40}'.format('DETECTOR DE PALÍNDROMO'))
frase = input('Escreva uma frase: ').strip().upper()

frase = frase.split()
junto = ''.join(frase)
inverso = ''

for i in range(len(junto) - 1, - 1, - 1):
    inverso += junto[i]
if junto == inverso:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo')