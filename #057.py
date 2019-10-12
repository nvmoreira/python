"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto."""

sexo = input('Sexo [F/M]: ').upper().strip()
while sexo not in 'F/M':
    sexo = input('Entrada incorreta, digite novamente. \nSexo [F/M]: ').upper().strip()
print('Sexo: {}'.format(sexo))
