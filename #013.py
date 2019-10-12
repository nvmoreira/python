# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

x = float(input('Digite o valor do salário: '))

aumento = (x * 15)/100
snovo = x + aumento

print('O valor do salário com 15% de aumento é de R${:.2f}'.format(snovo))