"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o
salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o
empréstimo será negado."""

print('COMPRE SUA CASA!!!')
casa = float(input('Qual o valor da casa que deseja comprar? '))
salario = float(input('Qual é o valor do seu salário? '))
tempo = float(input('Em quantos anos serão divididas as prestações? '))

prestacao = casa / (tempo * 12)
limite = salario * 30 / 100

if prestacao > limite:
    print('A prestação de R${:.2f} excede o limite de R${:.2f} do salário. Empréstimo negado.'.format(prestacao, limite))
else:
    print('Parabéns, seu empréstimo foi aprovado com parcelas de R${:.2f}!'.format(prestacao))