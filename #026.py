"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""

frase = input('Escreva uma frase: ').strip().upper()

quant = frase.count('A')
first = frase.find('A') + 1
last = frase.rfind('A') + 1

print("""Quantidade de letras "A": {}
Primeira aparição: {}
Última aparição : {}""".format(quant, first, last))
