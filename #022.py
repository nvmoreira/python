"""Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras no total, sem considerar espaços.
- Quantas letras tem o primeiro nome."""

nome = input('Escreva seu nome completo: ')

upper = nome.upper()
lower = nome.lower()
tamanho = len(nome) - nome.count(' ')
split = nome.split()
first = len(split[0])
showfirst = split[0]


print("""Seu nome em maiúsculas é {}
Seu nome em em minúsculas é {}
Seu nome possui {} letras ao todo
Seu primeiro nome é {} e possui {} letras.""".format(upper, lower, tamanho, showfirst, first))
