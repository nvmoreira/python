"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Digite o valor do salário: '))

if salario > 1250:
    aumento = (salario * 10) / 100
else:
    aumento = (salario * 15) / 100

total = salario + aumento

print('O aumento salarial recebido é de R${}, totalizando um salário de R${}.'.format(aumento, total))