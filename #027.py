"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente."""

nome = input('Escreva seu nome completo: ').strip().upper()

lista = nome.split()
tamanho = len(lista)
first = lista[0]
last = lista[tamanho - 1]

print("""Primeiro nome: {}
Último nome: {}""".format(first, last).title())
