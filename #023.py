# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

x = int(input('Escreva um número entre 0 e 9999: '))

unidade = x // 1 % 10
dezena = x // 10 % 10
centena = x // 100 % 10
milhar = x // 1000 % 10

print("""Analisando o número {}...
Unidade: {}
Dezena:  {}
Centena: {}
Milhar: {}""".format(x, unidade, dezena, centena, milhar))
