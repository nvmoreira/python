# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

x = float(input('Digite a quantidade de Km rodados com o carro: '))
y = int(input('Digite a quantidade de dias que o carro foi alugado: '))

km = x * 0.15
dias = y * 60
total = km + dias

print('O valor a ser pago pelo aluguel do carro é R${:.2f}.'.format(total))