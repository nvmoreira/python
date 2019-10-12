# Faça um algoritmo que leia um preço de um produto e mostre seu novo preço com 5% de desconto

x = float(input('Digite o valor do produto: '))

desconto = (x * 5)/100
pnovo = x - desconto

print('O preço do produto com 5% de desconto é R${:.2f}'.format(pnovo))